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
    def __init__(self, controller_TCP, controller_MODBUS, logger):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_MainWindow()
        # Setup the user interface
        self.ui.setupUi(self, controller_TCP, controller_MODBUS, logger)

class BANCO_DI_TARATURA:
    
    x=0
            
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
def run_logger(controller_modbus, controller_tcp, logger):
    logger.log_data(controller_TCP=controller_tcp, controller_MODBUS=controller_modbus)  
    
def data_update_mV(controller_modbus, controller_tcp, logger):
    while logger.DATA.loop_status:
        # print("data_update")
        result_list_laumas = controller_tcp.read_holding_registers_mV()   # celle di carico 1-4
        result_list_SG600 = controller_modbus.read_holding_registers_mV() # canale main e canale temp
        controller_tcp.DATA.LIST_mV_VALUE = result_list_laumas
        controller_modbus.DATA.canale_principale_mV = result_list_SG600[0]
        controller_modbus.DATA.canale_temperatura_mV = result_list_SG600[1]
        
def closed_last_window_signal(logger, window):
    logger.DATA.loop_status=False
    window.timerStop=True

# MAIN PER ESEGUIRE L'APPLICAZIONE
if __name__ == "__main__":
    controller_modbus=C_Seneca.Controller_MODBUS()
    controller_tcp=C_Laumas.Controller_TCP()
    logger=Logger.LOGGER(nome_CSV="Test")
    app = QApplication(sys.argv)
    window = MainWindow(controller_tcp, controller_modbus, logger)
    window.show()
    app.lastWindowClosed.connect(lambda: closed_last_window_signal(logger, window))
    logger_thread = Thread(target=run_logger, args=(controller_modbus, controller_tcp, logger))
    logger_thread.start()     
    update_thread = Thread(target=data_update_mV, args=(controller_modbus, controller_tcp, logger))
    update_thread.start()
    sys.exit(app.exec())