from __future__ import annotations
from PySide6.QtWidgets import QApplication, QSplashScreen
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QCursor, QPixmap
import controller_classes.Logger as Logger
import controller_classes.Controller_Client_TCP_Laumas as C_Laumas
import controller_classes.Controller_Client_MODBUS_Seneca as C_Seneca
from threading import Thread
from time import sleep
import time
from pymodbus import pymodbus_apply_logging_config
import sys
from PySide6.QtGui import QIcon
from logic_classes.View_QT_HomePage_logic import MainWindow
from logic_classes.Dialog_error_logic import Error_window
from Grafana_and_Influx.DB_Writer_Influx import DB_Writer
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import logging 
import os






class BANCO_DI_TARATURA:
    
    def __init__(self):
        
        logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        logging.warning('This will get logged to a file')
        
        self.controller_tcp=C_Laumas.Controller_TCP(self)
        self.controller_modbus=C_Seneca.Controller_MODBUS(self)
        self.logger=Logger.LOGGER(nome_CSV=None, banco_di_taratura=self, status=0, path_directory_CSV=None)
        self.db_writer=DB_Writer(self)
        
        # variabili per grafica
        self.window_icon_path = 'Assets/connection.png'
        
        # variabili per home page
        self.startStop = False
        self.status_pulsante_interfaccia = 1
        self.status_pulsante_registrazione = 1
        self.timerStop = False
        
        # variabili per setup page
        self.update_status = False
        self.list_status_checkbox_setup_page = [0,0,0,0]   #[CH4, CH3, CH2, CH1]     
        self.status_timer = False  
        self.m_main = 1
        self.q_main = 0
        self.m_temp = 1
        self.q_temp = 0
        
        # variabili per salvataggio setup file
        self.file_setup_banco_directory_path = None 
        self.file_setup_banco_name = None
        self.file_setup_euramet_directory_path = None 
        self.file_setup_euramet_name = None
        self.counter_salvataggio = 0
        
        # variabili per salvataggio registrazione
        self.registrazione_directory_path = None
        self.registrazione_name = None
        self.counter_registrazione = 0
        
        # variabili impostazione euramet
        self.list_status_checkbox_euramet_page = [0,0,1]   #[salita_1, discesa_1, salita_2]
        self.current_number_of_steps = 5
        self.status_inserimento_altezza = True
        self.quadrant = "Q1"
        
        # variabili excell euramet 
        self.euramet_unita_ingegneristica_di_misura = None
        self.euramet_Unità_ingegneristica_UUT = None
        '''self.euramet_Scale = self.controller_modbus.DATA.coefficiente_main''' #modifico direttamente il valore sul controller modbus
        self.euramet_Offset = None
        self.euramet_Coppia_taratura_MAX = 0
        self.euramet_Data = None
        self.euramet_Rif_interno_attivita = None
        self.euramet_Cliente = None
        self.euramet_SN_TX = None
        self.euramet_Descrizione_UUT = None
        self.euramet_Progetto_UUT = None
        self.euramet_SN_UUT = None
        self.euramet_Report_di_calibrazione_TX = None

        # variabili misura euramet
        self.axis_h = 837
        self.workbook = None
        self.euramet_cella_inizio_precarichi_Q3 = ["D",7]  # vorrei usarlo come "D7" ma devo cambiare D e 7 per spostarmi lungo il file excell
        self.euramet_cella_inizio_precarichi_Q1 = ["D",29]
        self.excell_path_template = 'Assets/04. YYMMDD - Rapporto Taratura UUT v9.xlsx'
        self.excell_file_name = None
        self.excell_path_dir_certificate = None
        self.excell_full_path = None
        self.excell_page_data = 'Euramet'
        self.excell_page_setup = 'Istruzioni Uso'
        
        # Variabili che gestiscono quanti quadranti ho passato
        self.quadrant_counter = 0
        
        # valori per plotting
        self.x = 0
        
        # valori per stabilità del led
        self.percentage_interval_green = 10
        self.percentage_interval_yellow = 15
        self.difference_variance_green = 1
        self.difference_variance_yellow = 3
        
    # metodi comuni a tutte le istanze da metter qui
    def set_window_icon(self, window:MainWindow):
        window.setWindowIcon(QIcon(self.window_icon_path))
        
    def error_window_logic(self, messaggio_di_errore="Errore. Qualcosa non funziona!", titolo="Error Window"):
        error_window = Error_window(banco_di_taratura=self)
        error_window.set_error_message(messaggio_di_errore)
        error_window.setWindowTitle(titolo)
        error_window.exec()
        

# FUNZIONI NECESSARIE PER I THREAD
def run_logger(controller_tcp:C_Laumas.Controller_TCP, controller_modbus:C_Seneca.Controller_MODBUS, logger:Logger.LOGGER):
    logger.log_data(controller_TCP=controller_tcp, controller_MODBUS=controller_modbus)  
    
def data_update_mV(controller_tcp:C_Laumas.Controller_TCP, controller_modbus:C_Seneca.Controller_MODBUS, logger:Logger.LOGGER):
    tmp = time.time()
    while logger.DATA.loop_status:
        try:
            # test = time.time() - tmp
            # print(f"tempo iniziale: {test}")
            # tmp = time.time()
            result_list_laumas = controller_tcp.read_holding_registers_mV()   # celle di carico 1-4
            # test = time.time() - tmp
            # print(f"tempo tcp: {test}")  # Tempo ottimizzato che richiede una scrittura e un loop di letture
            # tmp = time.time()
            result_list_SG600 = controller_modbus.read_holding_registers_mV() # canale main e canale temp
            # test = time.time() - tmp
            # print(f"tempo modbus: {test}")  # Tempo ottimizzato diccome la connessione funziona solo con un baudrate di 2400
            controller_tcp.DATA.LIST_mV_VALUE = result_list_laumas
            controller_modbus.DATA.canale_principale_mV = result_list_SG600[0]
            controller_modbus.DATA.canale_temperatura_mV = result_list_SG600[1]
            # tmp = time.time()
        except Exception as e:
            logging.critical("Problema critico nel dialogo con le schede!", exc_info=True)
            
def db_write(controller_tcp:C_Laumas.Controller_TCP, controller_modbus:C_Seneca.Controller_MODBUS, logger:Logger.LOGGER, db_writer:DB_Writer):
        
        # Dati registrati di Euramet
        list_main_temp = banco.logger.DATA.result_list_SG600_main_temp
        list_units_main_temp = banco.logger.DATA.text_lcd_SG600_main_temp
        list_units_laumas = banco.logger.DATA.text_lcd
        list_channels_laumas = banco.logger.DATA.result_list_1_4
        
        while banco.logger.DATA.loop_status:
            sleep(banco.logger.DATA.periodo_logger)
            if banco.logger.DATA.startStop_logger and db_writer != None:
                p = Point("Euramet Data").tag("measure", "measure")
                p.field("main", float(list_main_temp[0]))
                p.field("temp", float(list_main_temp[1]))
                p.field("CH1", float(list_channels_laumas[0]))
                p.field("CH2", float(list_channels_laumas[1]))
                p.field("CH3", float(list_channels_laumas[2]))
                p.field("CH4", float(list_channels_laumas[3]))
                db_writer.write_api.write(bucket=db_writer.bucket, org=db_writer.org, record=p)
                sleep(0.1)
    
        
def closed_last_window_signal(banco_di_taratura:BANCO_DI_TARATURA, window:MainWindow):
    banco_di_taratura.logger.DATA.loop_status=False
    window.timerStop=True

# MAIN PER ESEGUIRE L'APPLICAZIONE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    current_directory = os.getcwd()
    print(current_directory)
    
    # Setup splash screen
    splash_pix = QPixmap('Assets/output-onlinepngtools_resized.png')  # Use your own image path
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    
    banco=BANCO_DI_TARATURA()
    if banco.controller_tcp.connect():
        if banco.controller_modbus.connect():
            window = MainWindow(banco_di_taratura=banco)
            window.show()
            splash.finish(window)
            app.lastWindowClosed.connect(lambda: closed_last_window_signal(banco, window))
            logger_thread = Thread(target=run_logger, args=(banco.controller_tcp, banco.controller_modbus, banco.logger))
            logger_thread.start()     
            update_thread = Thread(target=data_update_mV, args=(banco.controller_tcp, banco.controller_modbus, banco.logger))
            update_thread.start()
            influx_thread = Thread(target=db_write, args=(banco.controller_tcp, banco.controller_modbus, banco.logger, banco.db_writer))
            influx_thread.start()
            sys.exit(app.exec())
        else:
            logging.error("Problema connessione con scheda Seneca", exc_info=True)
            banco.error_window_logic(messaggio_di_errore=f"ERROR! connessione fallita con scheda Seneca, chiudere la finestra\ne riavviare l'applicazione.")
            exit()
    else:
        logging.error("Problema connessione con scheda Laumas", exc_info=True)
        banco.error_window_logic(messaggio_di_errore=f"ERROR! connessione fallita con scheda Laumas, chiudere la finestra\ne riavviare l'applicazione.")
        exit()