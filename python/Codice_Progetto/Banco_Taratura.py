import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from View_QT_HomePage import Ui_MainWindow  # Import the generated UI class
import View_QT_HomePage
from View_QT_SetupPage import Ui_SetupWindow
import Logger as Logger
import Controller_Client_TCP_Laumas as C_Laumas
import Controller_Client_MODBUS_Seneca as C_Seneca
from threading import Thread
from time import sleep
from Dialog_setup_1_ui import Ui_Canale_Setup_1
from Dialog_setup_2_ui import Ui_Canale_Setup_2
from Dialog_setup_3_ui import Ui_Canale_Setup_3
from Dialog_setup_4_ui import Ui_Canale_Setup_4
from Dialog_setup_SG600_ui import Ui_SG600_Setup
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QTimer,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout, QDialog,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)



# DEFINIZIONE COSTRUTTORI PER LE VARIE FINESTRE DELL'APPLICAZIONE

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_MainWindow()
        # Setup the user interface
        self.ui.setupUi(self)
        
class SetupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_SetupWindow()
        # Setup the user interface
        self.ui.setupUi(self)
        
class Canale_Setup_1(QDialog):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_Canale_Setup_1()
        # Setup the user interface
        self.ui.setupUi(self)
        
class Canale_Setup_2(QDialog):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_Canale_Setup_2()
        # Setup the user interface
        self.ui.setupUi(self)
                
class Canale_Setup_3(QDialog):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_Canale_Setup_3()
        # Setup the user interface
        self.ui.setupUi(self)
        
class Canale_Setup_4(QDialog):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_Canale_Setup_4()
        # Setup the user interface
        self.ui.setupUi(self)
                        
class Canale_Setup_SG600(QDialog):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_SG600_Setup()
        # Setup the user interface
        self.ui.setupUi(self)

# DATI APPLICAZIONE

class SLAVE:        
    COM_port_Z4AI="COM8"
    baudrate_Z4AI=2400
    bytesize_Z4AI=8
    parity_Z4AI="N"
    stopbits_Z4AI=1
    ID_Z4AI=1
    
    ID_TLB4=1
    IP_TLB4="10.2.0.170"
    PORT_TLB4=10001
    BAUDRATE_TLB4=9600
    TIMEOUT_TLB4=5
    CHN_VOLTAGE_TLB4=5
    
class DATA:
    # status canale
    status_canali_SG600=0
    
    # main
    canale_principale_mV=0
    canale_principale_Nm=0
    sensibilità_principale=2.0000
    fondo_scala_principale=10000
    lever_length=1
    zero_main=0
    
    # temp
    canale_temperatura_mV=0
    canale_temperatura_C=0
    sensibilità_temperatura=0
    fondo_scala_temperatura=0
    zero_temp=0
    
    LIST_mV_VALUE = [0,0,0,0]   # Aggiornato dal main in un thread separato
    LIST_Kg_VALUE = [0,0,0,0]
    LIST_Nm_VALUE = [0,0,0,0]
    LIST_N_VALUE = [0,0,0,0]
    LIST_SENSIBILITY = [1,2.0302,0,1] # settato dalle varie setup pages
    LIST_FULLSCALE = [10,50,10,10] # settato dalle varie setup pages
    LIST_mV_ZERO = [1,-0.1,1,-0.21] # settato dalle varie setup pages
    LEVER_LENGTH = 1 # meters
    STATUS_CHANNELS = [0,0,0,0] # settato da setupPage

class ADDRESS:
    CMDR = 5
    REGISTER_SR1 = 6
    REGISTER_1_WR1_high = 50
    REGISTER_2_WR1_low = 51
    REGISTER_3 = 52
    REGISTER_AEXC = 61
    REGISTER_EXC = 63
    
class CMDR_COMMANDS:
    COMMAND_6902 = 6902
    COMMAND_6903 = 6903
    COMMAND_6808 = 6808
    DISABLE_command_cargo = 6809
    CHANNEL_command_search = 6094
    COMMAND_6563 = 6563
    COMMAND_6564 = 6564
    COMMAND_6703 = 6703
    COMMAND_6704 = 6704
    COMMAND_6575 = 6575
    COMMAND_6576 = 6576
    COMMAND_100 = 100
    COMMAND_25 = 25
    COMMAND_27 = 27
    ENABLE_command_dosage_read = 6803
    COMMAND_6501 = 6501
    COMMAND_6502 = 6502
    COMMAND_7 = 7
    COMMAND_9 = 9

     
class BANCO_DI_TARATURA:
    
    # """GETTERS TLB4 [scheda Laumas]"""
    
    # # GETTER INFO SLAVE TLB4
    # def get_slave_TLB4_id():
    #     return C_Laumas.SLAVE.ID
    # def get_slave_TLB4_port():
    #     return C_Laumas.SLAVE.PORT
    # def get_slave_TLB4_baudrate():
    #     return C_Laumas.SLAVE.BAUDRATE
    # def get_slave_TLB4_timeout():
    #     return C_Laumas.SLAVE.TIMEOUT
    # def get_slave_TLB4_ip():
    #     return C_Laumas.SLAVE.IP
    # def get_slave_TLB4_ChVoltage():   
    #     return C_Laumas.SLAVE.CHN_VOLTAGE
    
    # # GETTER INDIRIZZI REGISTRI DELLA SCHEDA [ indirizzo_vero-40001 = indirizzo_utilizzato ]
    # def get_TLB4_CMDR_address():
    #     return C_Laumas.ADDRESS.CMDR 
    # def get_TLB4_REGISTER_SR1_address():
    #     return C_Laumas.ADDRESS.REGISTER_SR1 
    # def get_TLB4_REGISTER_WR1_HIGH_address():
    #     return C_Laumas.ADDRESS.REGISTER_1_WR1_high 
    # def get_TLB4_REGISTER_WR1_LOW__address():
    #     return C_Laumas.ADDRESS.REGISTER_2_WR1_low
    # def get_TLB4_REGISTER_3_address(): 
    #     return C_Laumas.ADDRESS.REGISTER_3
    # def get_TLB4_REGISTER_AEXC_address():
    #     return C_Laumas.ADDRESS.REGISTER_AEXC 
    # def get_TLB4_REGISTER_EXC_address():
    #     return C_Laumas.ADDRESS.REGISTER_EXC
        
    # # GETTER DATI RELATIVI TLB4
    # # GETTER VALORI mV
    # def get_TLB4_CH1_value_mV():
    #     return C_Laumas.DATA.LIST_mV_VALUE[0]
    # def get_TLB4_CH2_value_mV():
    #     return C_Laumas.DATA.LIST_mV_VALUE[1]
    # def get_TLB4_CH3_value_mV():
    #     return C_Laumas.DATA.LIST_mV_VALUE[2]
    # def get_TLB4_CH4_value_mV():
    #     return C_Laumas.DATA.LIST_mV_VALUE[3]
    
    # # GETTER VALORI Kg
    # def get_TLB4_CH1_value_Kg():
    #     return C_Laumas.DATA.LIST_Kg_VALUE[0]
    # def get_TLB4_CH2_value_Kg():
    #     return C_Laumas.DATA.LIST_Kg_VALUE[1]
    # def get_TLB4_CH3_value_Kg():
    #     return C_Laumas.DATA.LIST_Kg_VALUE[2]
    # def get_TLB4_CH4_value_Kg():
    #     return C_Laumas.DATA.LIST_Kg_VALUE[3]    
    



    # FUNZIONI NECESSARIE PER I THREAD
    def run_logger():
        Logger.logger(nome_CSV= "test")  

    def data_update_mV():
        while Logger.DATA.loop_status:
            # print("data_update")
            result_list_laumas = C_Laumas.WORKING.read_holding_registers_mV()   # celle di carico 1-4
            result_list_SG600 = C_Seneca.WORKING.read_holding_registers_mV() # canale main e canale temp
            C_Laumas.DATA.LIST_mV_VALUE = result_list_laumas
            C_Seneca.DATA.canale_principale_mV = result_list_SG600[0]
            C_Seneca.DATA.canale_temperatura_mV = result_list_SG600[1]

    def closed_last_window_signal():
        Logger.DATA.loop_status=False
        View_QT_HomePage.timerStop=True
    
    # MAIN PER ESEGUIRE L'APPLICAZIONE
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.lastWindowClosed.connect(closed_last_window_signal)
        logger_thread = Thread(target=run_logger)
        logger_thread.start()     
        update_thread = Thread(target=data_update_mV)
        update_thread.start()
        sys.exit(app.exec())