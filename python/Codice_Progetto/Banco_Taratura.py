from __future__ import annotations
from PySide6.QtWidgets import QApplication
import controller_classes.Logger as Logger
import controller_classes.Controller_Client_TCP_Laumas as C_Laumas
import controller_classes.Controller_Client_MODBUS_Seneca as C_Seneca
from threading import Thread
from time import sleep
from pymodbus import pymodbus_apply_logging_config
import sys
from PySide6.QtGui import QIcon
from logic_classes.View_QT_HomePage_logic import MainWindow





class BANCO_DI_TARATURA:
    
    def __init__(self):
        self.controller_tcp=C_Laumas.Controller_TCP(self)
        self.controller_modbus=C_Seneca.Controller_MODBUS(self)
        self.logger=Logger.LOGGER(nome_CSV="Default", banco_di_taratura=self, status=0)
        
        # variabili per grafica
        self.window_icon_path = "python\\Codice_Progetto\\Assets\\connection.png"
        
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
        self.file_setup_banco_name = None
        self.file_setup_euramet_name = None
        self.counter_salvataggio = 0
        
        # variabili per salvataggio registrazione
        self.registrazione_name = None
        self.counter_registrazione = 0
        
        # variabili impostazione euramet
        self.list_status_checkbox_euramet_page = [0,0,1]   #[salita_1, discesa_1, salita_2]
        self.current_number_of_steps = 5
        self.status_inserimento_altezza = True
        self.quadrant = "Q1"
        
        # variabili csv euramet 
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
        self.excell_path_template = "python\\Codice_Progetto\\Template_Euramet_Excel\\04. YYMMDD - Rapporto Taratura UUT v9.xlsx"
        self.excell_name = "Default"
        self.excell_path_certificate =f"python\\Codice_Progetto\\Certificati_Euramet_Completi\\{self.excell_name}.xlsx"
        self.excell_page_data = "Euramet"
        self.excell_page_setup = "Istruzioni Uso"
        
        # Variabili che gestiscono quanti quadranti ho passato
        self.quadrant_counter = 0
        
        # valori per plotting
        self.x = 0
        
    # metodi comuni a tutte le istanze da metter qui
    def set_window_icon(self, window):
        window.setWindowIcon(QIcon(self.window_icon_path))


# FUNZIONI NECESSARIE PER I THREAD
def run_logger(controller_tcp:C_Laumas.Controller_TCP, controller_modbus:C_Seneca.Controller_MODBUS, logger:Logger.LOGGER):
    logger.log_data(controller_TCP=controller_tcp, controller_MODBUS=controller_modbus)  
    
def data_update_mV(controller_tcp:C_Laumas.Controller_TCP, controller_modbus:C_Seneca.Controller_MODBUS, logger:Logger.LOGGER):
    while logger.DATA.loop_status:
        # print("data_update")
        result_list_laumas = controller_tcp.read_holding_registers_mV()   # celle di carico 1-4
        result_list_SG600 = controller_modbus.read_holding_registers_mV() # canale main e canale temp
        controller_tcp.DATA.LIST_mV_VALUE = result_list_laumas
        controller_modbus.DATA.canale_principale_mV = result_list_SG600[0]
        controller_modbus.DATA.canale_temperatura_mV = result_list_SG600[1]
        
def closed_last_window_signal(banco_di_taratura:BANCO_DI_TARATURA, window:MainWindow):
    banco_di_taratura.logger.DATA.loop_status=False
    window.timerStop=True

# MAIN PER ESEGUIRE L'APPLICAZIONE
if __name__ == "__main__":
    banco=BANCO_DI_TARATURA()
    if banco.controller_tcp.connect():
        app = QApplication(sys.argv)
        window = MainWindow(banco_di_taratura=banco)
        window.show()
        app.lastWindowClosed.connect(lambda: closed_last_window_signal(banco, window))
        logger_thread = Thread(target=run_logger, args=(banco.controller_tcp, banco.controller_modbus, banco.logger))
        logger_thread.start()     
        update_thread = Thread(target=data_update_mV, args=(banco.controller_tcp, banco.controller_modbus, banco.logger))
        update_thread.start()
        sys.exit(app.exec())
    else:
        print("Problema connessione con scheda laumas")
        exit()