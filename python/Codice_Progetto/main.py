import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from View_QT_HomePage import Ui_MainWindow  # Import the generated UI class
from View_QT_SetupPage import Ui_SetupWindow
import Logger as Logger
import Controller_Client_TCP
from threading import Thread
from time import sleep


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_MainWindow()
        # Setup the user interface
        self.ui.setupUi(self)


def run_logger():
    Logger.logger(nome_CSV= "test")  

def data_update_mV():
    while Logger.DATA.loop_status:
        result_list = Controller_Client_TCP.WORKING.read_holding_registers_mV()
        Controller_Client_TCP.DATA.LIST_mV_VALUE = result_list

def closed_last_window_signal():
    Logger.DATA.loop_status=False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.lastWindowClosed.connect(closed_last_window_signal)
    # Create and start a thread for the logger and for data acquisition
    logger_thread = Thread(target=run_logger)
    logger_thread.start()     
    update_thread = Thread(target=data_update_mV)
    update_thread.start()
    sys.exit(app.exec())


    