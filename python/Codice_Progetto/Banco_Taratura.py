import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import View_QT_HomePage      # Import the generated UI class
import Logger as Logger
import Controller_Client_TCP_Laumas as C_Laumas
import Controller_Client_MODBUS_Seneca as C_Seneca
from threading import Thread
from time import sleep
from pymodbus import pymodbus_apply_logging_config
from time import sleep
import sys





class BANCO_DI_TARATURA:
    
    def __init__(self):
        self.controller_tcp=C_Laumas.Controller_TCP()
        self.controller_modbus=C_Seneca.Controller_MODBUS()
        self.logger=Logger.LOGGER(nome_CSV="Test")
        
        # variabili per home page
        self.startStop = False
        self.status_pulsante_interfaccia = 1
        self.status_pulsante_registrazione = 1
        self.timerStop = False
        
        # variabili per setup page
        self.update_status = False
        self.list_status_checkbox = [0,0,0,0]   #[CH4, CH3, CH2, CH1]     
        self.status_timer = False  
        
    # metodi comuni a tutte le istanze da metter qui



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
        
def closed_last_window_signal(banco_di_taratura:BANCO_DI_TARATURA, window:QMainWindow):
    banco_di_taratura.logger.DATA.loop_status=False
    window.timerStop=True

# MAIN PER ESEGUIRE L'APPLICAZIONE
if __name__ == "__main__":
    banco=BANCO_DI_TARATURA()
    app = QApplication(sys.argv)
    window = View_QT_HomePage.MainWindow(banco_di_taratura=banco)
    window.show()
    app.lastWindowClosed.connect(lambda: closed_last_window_signal(banco, window))
    logger_thread = Thread(target=run_logger, args=(banco.controller_tcp, banco.controller_modbus, banco.logger))
    logger_thread.start()     
    update_thread = Thread(target=data_update_mV, args=(banco.controller_tcp, banco.controller_modbus, banco.logger))
    update_thread.start()
    sys.exit(app.exec())