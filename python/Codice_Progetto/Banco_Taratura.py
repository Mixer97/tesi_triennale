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
from pymodbus.client import ModbusTcpClient
from pymodbus.client import ModbusSerialClient
from pymodbus.framer import Framer
from pymodbus import pymodbus_apply_logging_config
from time import sleep
import sys
import serial



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





class BANCO_DI_TARATURA:
    
    
  
    # class Z4AI: 
        
    #     class SLAVE:       
    #         Z4AI_COM_port="COM8"
    #         Z4AI_baudrate=2400
    #         Z4AI_bytesize=8
    #         Z4AI_parity="N"
    #         Z4AI_stopbits=1
    #         Z4AI_ID=1
            
    #     class DATA:
    #         # status canale
    #         Z4AI_status_canali_SG600=0
            
    #         # main
    #         Z4AI_canale_principale_mV=0
    #         Z4AI_canale_principale_Nm=0
    #         Z4AI_sensibilità_principale=2.0000
    #         Z4AI_fondo_scala_principale=10000
    #         Z4AI_lever_length=1
    #         Z4AI_zero_main=0
            
    #         # temp
    #         Z4AI_canale_temperatura_mV=0
    #         Z4AI_canale_temperatura_C=0
    #         Z4AI_sensibilità_temperatura=0
    #         Z4AI_fondo_scala_temperatura=0
    #         Z4AI_zero_temp=0
    
    # class TLB4: 
        
    #     class SLAVE:  
    #         TLB4_ID=1
    #         TLB4_IP="10.2.0.170"
    #         TLB4_PORT=10001
    #         TLB4_BAUDRATE=9600
    #         TLB4_TIMEOUT=5
    #         TLB4_CHN_VOLTAGE=5
        
    #     class DATA:
    #         TLB4_LIST_mV_VALUE = [0,0,0,0]   # Aggiornato dal main in un thread separato
    #         TLB4_LIST_Kg_VALUE = [0,0,0,0]
    #         TLB4_LIST_Nm_VALUE = [0,0,0,0]
    #         TLB4_LIST_N_VALUE = [0,0,0,0]
    #         TLB4_LIST_SENSIBILITY = [1,2.0302,0,1] # settato dalle varie setup pages
    #         TLB4_LIST_FULLSCALE = [10,50,10,10] # settato dalle varie setup pages
    #         TLB4_LIST_mV_ZERO = [1,-0.1,1,-0.21] # settato dalle varie setup pages
    #         TLB4_LEVER_LENGTH = 1 # meters
    #         TLB4_STATUS_CHANNELS = [0,0,0,0] # settato da setupPage

    #     class ADDRESS:
    #         TLB4_CMDR = 5
    #         TLB4_REGISTER_SR1 = 6
    #         TLB4_REGISTER_1_WR1_high = 50
    #         TLB4_REGISTER_2_WR1_low = 51
    #         TLB4_REGISTER_3 = 52
    #         TLB4_REGISTER_AEXC = 61
    #         TLB4_REGISTER_EXC = 63
        
    #     class CMDR_COMMANDS:
    #         TLB4_COMMAND_6902 = 6902
    #         TLB4_COMMAND_6903 = 6903
    #         TLB4_COMMAND_6808 = 6808
    #         TLB4_DISABLE_command_cargo = 6809
    #         TLB4_CHANNEL_command_search = 6094
    #         TLB4_COMMAND_6563 = 6563
    #         TLB4_COMMAND_6564 = 6564
    #         TLB4_COMMAND_6703 = 6703
    #         TLB4_COMMAND_6704 = 6704
    #         TLB4_COMMAND_6575 = 6575
    #         TLB4_COMMAND_6576 = 6576
    #         TLB4_COMMAND_100 = 100
    #         TLB4_COMMAND_25 = 25
    #         TLB4_COMMAND_27 = 27
    #         TLB4_ENABLE_command_dosage_read = 6803
    #         TLB4_COMMAND_6501 = 6501
    #         TLB4_COMMAND_6502 = 6502
    #         TLB4_COMMAND_7 = 7
    #         TLB4_COMMAND_9 = 9
            
    # class GETTERS_TLB4_DATA:
        
    #     # mV
    #     def get_TLB4_CH1_mV_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_mV_VALUE[3]
    #     def get_TLB4_CH2_mV_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_mV_VALUE[2]
    #     def get_TLB4_CH3_mV_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_mV_VALUE[1]
    #     def get_TLB4_CH4_mV_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_mV_VALUE[0]
        
    #     # Kg
    #     def get_TLB4_CH1_Kg_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_Kg_VALUE[3]
    #     def get_TLB4_CH2_Kg_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_Kg_VALUE[2]
    #     def get_TLB4_CH3_Kg_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_Kg_VALUE[1]
    #     def get_TLB4_CH4_Kg_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_Kg_VALUE[0]
        
    #     # Nm
    #     def get_TLB4_CH1_Nm_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_Nm_VALUE[3]
    #     def get_TLB4_CH2_Nm_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_Nm_VALUE[2]
    #     def get_TLB4_CH3_Nm_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_Nm_VALUE[1]
    #     def get_TLB4_CH4_Nm_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_Nm_VALUE[0]
        
    #     # N
    #     def get_TLB4_CH1_N_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_N_VALUE[3]
    #     def get_TLB4_CH2_N_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_N_VALUE[2]
    #     def get_TLB4_CH3_N_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_N_VALUE[1]
    #     def get_TLB4_CH4_N_Value():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_N_VALUE[0]
        
    #     # Sensibilità
    #     def get_TLB4_CH1_SENSIBILITY():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_SENSIBILITY[3]
    #     def get_TLB4_CH2_SENSIBILITY():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_SENSIBILITY[2]
    #     def get_TLB4_CH3_SENSIBILITY():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_SENSIBILITY[1]
    #     def get_TLB4_CH4_SENSIBILITY():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_SENSIBILITY[0]
        
    #     # Fondoscala
    #     def get_TLB4_CH1_FULLSCALE():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_FULLSCALE[3]
    #     def get_TLB4_CH2_FULLSCALE():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_FULLSCALE[2]
    #     def get_TLB4_CH3_FULLSCALE():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_FULLSCALE[1]
    #     def get_TLB4_CH4_FULLSCALE():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_FULLSCALE[0]
        
    #     # Zeri
    #     def get_TLB4_CH1_mV_ZERO():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_mV_ZERO[3]
    #     def get_TLB4_CH2_mV_ZERO():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_mV_ZERO[2]
    #     def get_TLB4_CH3_mV_ZERO():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_mV_ZERO[1]
    #     def get_TLB4_CH4_mV_ZERO():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_LIST_mV_ZERO[0]
    
    #     # Status canali
    #     def get_TLB4_CH1_STATUS_CHANNELS():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_STATUS_CHANNELS[3]
    #     def get_TLB4_CH2_STATUS_CHANNELS():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_STATUS_CHANNELS[2]
    #     def get_TLB4_CH3_STATUS_CHANNELS():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_STATUS_CHANNELS[1]
    #     def get_TLB4_CH4_STATUS_CHANNELS():
    #         return BANCO_DI_TARATURA.TLB4.DATA.TLB4_STATUS_CHANNELS[0]

    # class GETTERS_Z4AI_DATA:
    #     pass
    
    # class SETTERS_TLB4_DATA:
    #     pass
    
    # class SETTERS_Z4AI_DATA:
    #     pass




    # client_TLB4 = ModbusTcpClient(host=TLB4.SLAVE.TLB4_IP,
    #                               port=TLB4.SLAVE.TLB4_PORT,
    #                               baudrate=TLB4.SLAVE.TLB4_BAUDRATE,
    #                               timeout=TLB4.SLAVE.TLB4_TIMEOUT,
    #                               framer=Framer.RTU
    #                               )

    # client_Z4AI = ModbusSerialClient(method='rtu',
    #                             port=Z4AI.SLAVE.Z4AI_COM_port,
    #                             baudrate=Z4AI.SLAVE.Z4AI_baudrate,
    #                             bytesize=Z4AI.SLAVE.Z4AI_bytesize,
    #                             parity=Z4AI.SLAVE.Z4AI_parity,
    #                             stopbits=Z4AI.SLAVE.Z4AI_stopbits
    #                             )









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