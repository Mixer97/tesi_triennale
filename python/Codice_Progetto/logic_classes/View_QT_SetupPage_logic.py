from __future__ import annotations
from PySide6.QtCore import QTimer, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QFileDialog
from qt_classes.View_QT_SetupPage_ui import Ui_SetupWindow
from logic_classes.Dialog_setup_1_logic import Canale_Setup_1
from logic_classes.Dialog_setup_2_logic import Canale_Setup_2
from logic_classes.Dialog_setup_3_logic import Canale_Setup_3
from logic_classes.Dialog_setup_4_logic import Canale_Setup_4
from logic_classes.Dialog_setup_SG600_logic import Canale_Setup_SG600
from logic_classes.Dialog_salavataggio_setup_logic import Salvataggio_setup
from logic_classes.Handler_JSON import handler_json
from logic_classes.Dialog_error_logic import Error_window
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from View_QT_HomePage_logic import MainWindow



class SetupWindow(QMainWindow):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, homepage:MainWindow):
        super().__init__()
        self.banco_di_taratura = banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_SetupWindow()
        # Setup the user interface
        self.ui.setupUi(self)
        self.homepage = homepage
        self.setWindowTitle(QCoreApplication.translate("SetupWindow", u"Setup Window", None))
        self.banco_di_taratura.set_window_icon(self)

        self.controller_TCP = banco_di_taratura.controller_tcp
        self.controller_MODBUS = banco_di_taratura.controller_modbus
        self.logger = banco_di_taratura.logger
        
        self.update_status = banco_di_taratura.update_status # bool [FALSE]
        self.list_status_checkbox = banco_di_taratura.list_status_checkbox_setup_page  # list status ordine:  [ch4, ch3, ch2, ch1]
        self.status_timer = banco_di_taratura.status_timer  # bool [FALSE]
        
        self.finestra_salvataggio_setup = Salvataggio_setup(self.banco_di_taratura, self)
        
        self.setWindowTitle(QCoreApplication.translate("SetupWindow", u"Setup Window", None))
        
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
        self.ui.lcdNumber_coefficiente_CHSG600.setDigitCount(7)
        self.ui.lcdNumber_coefficiente_CHSG600_temp.setDigitCount(7)
        
        self.ui.lcdNumber_CH1_2.display(self.controller_TCP.DATA.LIST_FULLSCALE[0])
        self.ui.lcdNumber_CH2_2.display(self.controller_TCP.DATA.LIST_FULLSCALE[1])
        self.ui.lcdNumber_CH3_2.display(self.controller_TCP.DATA.LIST_FULLSCALE[2])
        self.ui.lcdNumber_CH4_2.display(self.controller_TCP.DATA.LIST_FULLSCALE[3])
        self.ui.lcdNumber_CH1.display(self.controller_TCP.DATA.LIST_SENSIBILITY[0])
        self.ui.lcdNumber_CH2.display(self.controller_TCP.DATA.LIST_SENSIBILITY[1])
        self.ui.lcdNumber_CH3.display(self.controller_TCP.DATA.LIST_SENSIBILITY[2])
        self.ui.lcdNumber_CH4.display(self.controller_TCP.DATA.LIST_SENSIBILITY[3])
        self.ui.lcdNumber_coefficiente_CHSG600.display(self.controller_MODBUS.DATA.coefficiente_main)
        self.ui.lcdNumber_coefficiente_CHSG600_temp.display(self.controller_MODBUS.DATA.coefficiente_temp)
        
        # controllo i canali attivi nella scheda e faccio corrispodere la grafica
        if self.list_status_checkbox[3] == 1:
                self.ui.checkBox_CH1.setChecked(True)
                self.ui.checkBox_CH1.setText("ON")
        if self.list_status_checkbox[2] == 1:
                self.ui.checkBox_CH2.setChecked(True)
                self.ui.checkBox_CH2.setText("ON")
        if self.list_status_checkbox[1] == 1:
                self.ui.checkBox_CH3.setChecked(True)
                self.ui.checkBox_CH3.setText("ON")
        if self.list_status_checkbox[0] == 1:
                self.ui.checkBox_CH4.setChecked(True)
                self.ui.checkBox_CH4.setText("ON")
        
        self.timer1 = QTimer()
        
        # setup dei segnali
        self.ui.checkBox_CH1.stateChanged.connect(lambda: self.on_click(1))  # labda: va usato se voglio inserire dei parametri
        self.ui.checkBox_CH2.stateChanged.connect(lambda: self.on_click(2))
        self.ui.checkBox_CH3.stateChanged.connect(lambda: self.on_click(3))
        self.ui.checkBox_CH4.stateChanged.connect(lambda: self.on_click(4))
        self.ui.pushButton_concludi_setup.clicked.connect(self.finalizing_setup)
        self.ui.pushButton_setup_CH1.clicked.connect(self.open_setup_CH1_window)
        self.ui.pushButton_setup_CH2.clicked.connect(self.open_setup_CH2_window)
        self.ui.pushButton_setup_CH3.clicked.connect(self.open_setup_CH3_window)
        self.ui.pushButton_setup_CH4.clicked.connect(self.open_setup_CH4_window)
        self.ui.pushButton_setup_CHSG600.clicked.connect(self.open_setup_SG600_window)
        self.ui.pushButton_salvataggio_setup.clicked.connect(self.save_banco_setup)
        self.ui.pushButton_carica_setup.clicked.connect(self.load_banco_setup)
        
        # segnale per ritorno alla homapage
        self.ui.pushButton_home.clicked.connect(self.show_home_window)
        
    def show_home_window(self):
        self.homepage.show()
        self.close()
        
    def save_banco_setup(self):
        dname = QFileDialog.getExistingDirectory()
        if dname != '':
            self.banco_di_taratura.file_setup_banco_directory_path = dname
            self.finestra_salvataggio_setup.exec()
        else:
                self.banco_di_taratura.error_window_logic("Path non selezionato!")
        
    def open_setup_CH1_window(self):
        self.setup_window = Canale_Setup_1(banco_di_taratura=self.banco_di_taratura, setup_window=self)
        self.setup_window.exec()
        self.ui.pushButton_concludi_setup.click()
        
    def open_setup_CH2_window(self):
        self.setup_window = Canale_Setup_2(banco_di_taratura=self.banco_di_taratura, setup_window=self)
        self.setup_window.exec()
        self.ui.pushButton_concludi_setup.click()

    def open_setup_CH3_window(self):
        self.setup_window = Canale_Setup_3(banco_di_taratura=self.banco_di_taratura, setup_window=self)
        self.setup_window.exec()
        self.ui.pushButton_concludi_setup.click()

    def open_setup_CH4_window(self):
        self.setup_window = Canale_Setup_4(banco_di_taratura=self.banco_di_taratura, setup_window=self)
        self.setup_window.exec()
        self.ui.pushButton_concludi_setup.click()
        
    def open_setup_SG600_window(self):
        self.setup_window = Canale_Setup_SG600(banco_di_taratura=self.banco_di_taratura)
        self.setup_window.setWindowTitle("SG600 Setup Window")
        self.setup_window.exec()
        self.ui.pushButton_concludi_setup.click()
    
    def load_banco_setup(self):
        fname = QFileDialog.getOpenFileName() # prendi info del file selezionato
        fname = fname[0]    # dalle info estrae il path assoluto
        if fname.endswith('json'):  # controllo sia un json
            tmp=handler_json(path_file_load=fname)
            tmp.load_setup_banco(banco_di_taratura=self.banco_di_taratura, setup_window=self)
            self.ui.pushButton_concludi_setup.click()
        else:   # finestra di errore
            error_window = Error_window(banco_di_taratura=self.banco_di_taratura)
            error_window.set_error_message("Errore nella selezione del file (file selezionato non è .json)")
            error_window.setWindowTitle("Error Window")
            error_window.exec()
    
    # Funzione per gestire i canali attivi/disattivi con un click
    def on_click(self, ID):  
        self.list_status_checkbox[abs(ID-4)] = int(not(self.list_status_checkbox[abs(ID-4)]))
        print("STATUS CHN" + str(ID) + " = " + str(self.list_status_checkbox[abs(ID-4)]) + "; status-checkbox = " + str(self.list_status_checkbox))
        self.ui.pushButton_concludi_setup.click()
    
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
        self.ui.lcdNumber_coefficiente_CHSG600.display(self.controller_MODBUS.DATA.coefficiente_main)
        self.ui.lcdNumber_coefficiente_CHSG600_temp.display(self.controller_MODBUS.DATA.coefficiente_temp)
        
        # Updtate dei testi dei checkbox
        if self.list_status_checkbox[3]==0:
            self.ui.checkBox_CH1.setText('OFF')
        else:
            self.ui.checkBox_CH1.setText('ON')
        
        if self.list_status_checkbox[2]==0:
            self.ui.checkBox_CH2.setText('OFF')
        else:
            self.ui.checkBox_CH2.setText('ON')
            
        if self.list_status_checkbox[1]==0:
            self.ui.checkBox_CH3.setText('OFF')
        else:
            self.ui.checkBox_CH3.setText('ON')
            
        if self.list_status_checkbox[0]==0:
            self.ui.checkBox_CH4.setText('OFF')
        else:
            self.ui.checkBox_CH4.setText('ON')