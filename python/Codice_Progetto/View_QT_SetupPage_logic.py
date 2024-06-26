from __future__ import annotations
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow
from View_QT_SetupPage import Ui_SetupWindow
from Dialog_setup_1_logic import Canale_Setup_1
from Dialog_setup_2_logic import Canale_Setup_2
from Dialog_setup_3_logic import Canale_Setup_3
from Dialog_setup_4_logic import Canale_Setup_4
from Dialog_setup_SG600_logic import Canale_Setup_SG600
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA



class SetupWindow(QMainWindow):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA):
        super().__init__()
        self.banco_di_taratura = banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_SetupWindow()
        # Setup the user interface
        self.ui.setupUi(self)

        self.controller_TCP = banco_di_taratura.controller_tcp
        self.controller_MODBUS = banco_di_taratura.controller_modbus
        self.logger = banco_di_taratura.logger
        
        self.update_status = banco_di_taratura.update_status # bool [FALSE]
        self.list_status_checkbox = banco_di_taratura.list_status_checkbox  # list
        self.status_timer = banco_di_taratura.status_timer  # bool [FALSE]
        
        while self.list_status_checkbox == [0,0,0,0]:     
            self.list_status_checkbox=self.controller_TCP.read_channels_active() 
            
            


        # Imposto sensibilità, fondoscala e numero di cifre dei canali
        self.ui.lcdNumber_CH1_2.setDigitCount(7)
        self.ui.lcdNumber_CH2_2.setDigitCount(7)
        self.ui.lcdNumber_CH3_2.setDigitCount(7)
        self.ui.lcdNumber_CH4_2.setDigitCount(7)
        self.ui.lcdNumber_CH1.setDigitCount(7)
        self.ui.lcdNumber_CH2.setDigitCount(7)
        self.ui.lcdNumber_CH3.setDigitCount(7)
        self.ui.lcdNumber_CH4.setDigitCount(7)
        self.ui.lcdNumber_fondoscala_CHSG600.setDigitCount(7)
        self.ui.lcdNumber_sens_CHSG600.setDigitCount(7)
        
        self.ui.lcdNumber_CH1_2.display(self.controller_TCP.DATA.LIST_FULLSCALE[0])
        self.ui.lcdNumber_CH2_2.display(self.controller_TCP.DATA.LIST_FULLSCALE[1])
        self.ui.lcdNumber_CH3_2.display(self.controller_TCP.DATA.LIST_FULLSCALE[2])
        self.ui.lcdNumber_CH4_2.display(self.controller_TCP.DATA.LIST_FULLSCALE[3])
        self.ui.lcdNumber_CH1.display(self.controller_TCP.DATA.LIST_SENSIBILITY[0])
        self.ui.lcdNumber_CH2.display(self.controller_TCP.DATA.LIST_SENSIBILITY[1])
        self.ui.lcdNumber_CH3.display(self.controller_TCP.DATA.LIST_SENSIBILITY[2])
        self.ui.lcdNumber_CH4.display(self.controller_TCP.DATA.LIST_SENSIBILITY[3])
        self.ui.lcdNumber_fondoscala_CHSG600.display(self.controller_MODBUS.DATA.fondo_scala_principale)
        self.ui.lcdNumber_sens_CHSG600.display(self.controller_MODBUS.DATA.sensibilità_principale)
        
        # controllo i canali attivi nella scheda e faccio corrispodere la grafica
        if self.list_status_checkbox[3] == 1:
                self.ui.checkBox_CH1.setChecked(True)
        if self.list_status_checkbox[2] == 1:
                self.ui.checkBox_CH2.setChecked(True)
        if self.list_status_checkbox[1] == 1:
                self.ui.checkBox_CH3.setChecked(True)
        if self.list_status_checkbox[0] == 1:
                self.ui.checkBox_CH4.setChecked(True)
        
        self.timer1 = QTimer()
        
        # setup dei segnali
        self.ui.checkBox_CH1.stateChanged.connect(lambda: self.on_click(1))
        self.ui.checkBox_CH2.stateChanged.connect(lambda: self.on_click(2))
        self.ui.checkBox_CH3.stateChanged.connect(lambda: self.on_click(3))
        self.ui.checkBox_CH4.stateChanged.connect(lambda: self.on_click(4))
        self.ui.pushButton_concludi_setup.clicked.connect(self.finalizing_setup)
        self.ui.pushButton_setup_CH1.clicked.connect(self.open_setup_CH1_window)
        self.ui.pushButton_setup_CH2.clicked.connect(self.open_setup_CH2_window)
        self.ui.pushButton_setup_CH3.clicked.connect(self.open_setup_CH3_window)
        self.ui.pushButton_setup_CH4.clicked.connect(self.open_setup_CH4_window)
        self.ui.pushButton_setup_CHSG600.clicked.connect(self.open_setup_SG600_window)
        
        
    def open_setup_CH1_window(self):
        self.setup_window = Canale_Setup_1(banco_di_taratura=self.banco_di_taratura)
        self.setup_window.show()
        
    def open_setup_CH2_window(self):
        self.setup_window = Canale_Setup_2(banco_di_taratura=self.banco_di_taratura)
        self.setup_window.show()

    def open_setup_CH3_window(self):
        self.setup_window = Canale_Setup_3(banco_di_taratura=self.banco_di_taratura)
        self.setup_window.show()

    def open_setup_CH4_window(self):
        self.setup_window = Canale_Setup_4(banco_di_taratura=self.banco_di_taratura)
        self.setup_window.show()
        
    def open_setup_SG600_window(self):
        self.setup_window = Canale_Setup_SG600(banco_di_taratura=self.banco_di_taratura)
        self.setup_window.show()
        
    
    # Funzione per gestire i canali attivi/disattivi con un click
    def on_click(self, ID):  
        self.list_status_checkbox[abs(ID-4)] = int(not(self.list_status_checkbox[abs(ID-4)]))
        print("STATUS CHN" + str(ID) + " = " + str(self.list_status_checkbox[abs(ID-4)]) + "; status-checkbox = " + str(self.list_status_checkbox))
    
    # Impostazioni vengono salvate definitivamente nella scheda a seguito di questa funzione
    def finalizing_setup(self):
        if self.list_status_checkbox == [0,0,0,0]:      # Controllo che la configurazione sia valida
                print("Configurazione invalida, ripristino alla configurazione base con canale 1 ON.")
                self.ui.checkBox_CH1.setChecked(True)
        print(self.list_status_checkbox)
        self.controller_TCP.setup_full_update(self.list_status_checkbox)
        # sleep(0.2)
        self.ui.lcdNumber_CH1_2.display(self.controller_TCP.DATA.LIST_FULLSCALE[0])
        self.ui.lcdNumber_CH2_2.display(self.controller_TCP.DATA.LIST_FULLSCALE[1])
        self.ui.lcdNumber_CH3_2.display(self.controller_TCP.DATA.LIST_FULLSCALE[2])
        self.ui.lcdNumber_CH4_2.display(self.controller_TCP.DATA.LIST_FULLSCALE[3])
        self.ui.lcdNumber_CH1.display(self.controller_TCP.DATA.LIST_SENSIBILITY[0])
        self.ui.lcdNumber_CH2.display(self.controller_TCP.DATA.LIST_SENSIBILITY[1])
        self.ui.lcdNumber_CH3.display(self.controller_TCP.DATA.LIST_SENSIBILITY[2])
        self.ui.lcdNumber_CH4.display(self.controller_TCP.DATA.LIST_SENSIBILITY[3])
        self.ui.lcdNumber_fondoscala_CHSG600.display(self.controller_MODBUS.DATA.fondo_scala_principale)
        self.ui.lcdNumber_sens_CHSG600.display(self.controller_MODBUS.DATA.sensibilità_principale)