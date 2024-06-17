import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from View_QT_HomePage import Ui_MainWindow  # Import the generated UI class
import View_QT_HomePage
from View_QT_SetupPage import Ui_SetupWindow
import Logger as Logger
import Controller_Client_TCP_Laumas as Controller_Client_TCP_Laumas
import Controller_Client_MODBUS_Seneca
from threading import Thread
from time import sleep


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_MainWindow()
        # Setup the user interface
        self.ui.setupUi(self)

def run_logger(controller_modbus, controller_tcp):
    Logger.LOGGER("test", controller_modbus, controller_tcp)  

def data_update_mV():
    while Logger.DATA.loop_status:
        # print("data_update")
        result_list_laumas = Controller_Client_TCP_Laumas.WORKING.read_holding_registers_mV()   # celle di carico 1-4
        result_list_SG600 = Controller_Client_MODBUS_Seneca.WORKING.read_holding_registers_mV() # canale main e canale temp
        Controller_Client_TCP_Laumas.DATA.LIST_mV_VALUE = result_list_laumas
        Controller_Client_MODBUS_Seneca.DATA.canale_principale_mV = result_list_SG600[0]
        Controller_Client_MODBUS_Seneca.DATA.canale_temperatura_mV = result_list_SG600[1]

def closed_last_window_signal():
    Logger.DATA.loop_status=False
    View_QT_HomePage.timerStop=True
    


if __name__ == "__main__":
    controller_modbus=Controller_Client_MODBUS_Seneca()
    controller_tcp=Controller_Client_TCP_Laumas()
    
    # Create and start a thread for the logger and for data acquisition    
    logger_thread = Thread(target=run_logger, args=(controller_modbus, controller_tcp))
    logger_thread.start()     
    update_thread = Thread(target=data_update_mV)
    update_thread.start()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.lastWindowClosed.connect(closed_last_window_signal)
    sys.exit(app.exec())


    