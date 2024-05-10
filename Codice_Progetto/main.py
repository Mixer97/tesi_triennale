import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from QT_Creator_dell_App_4_ui import Ui_MainWindow  # Import the generated UI class
import logger_CSV_Inserisco_direttamente
from threading import Thread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_MainWindow()
        # Setup the user interface
        self.ui.setupUi(self)
        # Create and start a thread for the logger
        logger_thread = Thread(target=run_logger)
        logger_thread.start()        

def run_logger():
    logger_CSV_Inserisco_direttamente.logger()  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    