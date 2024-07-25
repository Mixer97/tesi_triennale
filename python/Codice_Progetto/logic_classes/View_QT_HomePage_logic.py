from __future__ import annotations
from PySide6.QtCore import QTimer, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QFileDialog
from qt_classes.View_QT_HomePage_ui import Ui_MainWindow
from logic_classes.View_QT_SetupPage_logic import SetupWindow
from logic_classes.Mainwindow_grafico_logic import GraphWindow
from logic_classes.Dialog_salavataggio_registrazione_logic import Salvataggio_registrazione
from typing import TYPE_CHECKING
from logic_classes.Dialog_error_logic import Error_window
import logging
import time

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA


class MainWindow(QMainWindow):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA):
        super().__init__()
        self.banco_di_taratura = banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_MainWindow()
        # Setup the user interface
        self.ui.setupUi(self)
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main Window", None))
        self.banco_di_taratura.set_window_icon(self)
        
        
        self.logger = banco_di_taratura.logger
        self.controller_TCP = banco_di_taratura.controller_tcp
        self.controller_MODBUS = banco_di_taratura.controller_modbus
        
        self.startStop = banco_di_taratura.startStop
        self.status_pulsante_interfaccia = banco_di_taratura.status_pulsante_interfaccia
        self.status_pulsante_registrazione = banco_di_taratura.status_pulsante_registrazione
        self.timerStop = banco_di_taratura.timerStop
        
        self.setup_window = SetupWindow(self.banco_di_taratura, self)
        self.setup_graph = GraphWindow(self.banco_di_taratura, self)
        self.setup_graph.setWindowTitle("Graph Window")
        self.finestra_salvataggio_registrazione = Salvataggio_registrazione(self.banco_di_taratura, self)
    
    # setup segnali
        self.ui.pushButton_Interfaccia.clicked.connect(self.pulsante_interfaccia_click)  # pulsanti interfaccia e registrazione
        self.ui.pushButton_Registrazione.clicked.connect(self.pulsante_registrazione_click)  
        self.timer1 = QTimer()     # Timer
        self.timer2 = QTimer()  
        self.timer2.start(100)
        self.timer1.timeout.connect(self.update_CH1)   # Update degli lcd
        self.timer1.timeout.connect(self.update_CH2)                        
        self.timer1.timeout.connect(self.update_CH3)                        
        self.timer1.timeout.connect(self.update_CH4)                           
        self.timer1.timeout.connect(self.update_SG600_main)              
        self.timer1.timeout.connect(self.update_SG600_temp)              
        self.timer2.timeout.connect(self.setter_lcdDisplay_text_logger)                             
        self.ui.pushButton_setup_page.clicked.connect(self.show_setup_window) 
        self.pulsante_interfaccia_click()               # click iniziale per avviare l'interfaccia             
        self.timer1.timeout.connect(self.check)         # Check per chiusura dei timer alla chiusura dell'ultima finestra
        # self.show_graph_window()                        # Mostra la finestra con il grafico all' apertura
        self.ui.pushButton_grafico.clicked.connect(self.show_graph_window)
        self.ui.pushButton_setup_registrazione.clicked.connect(self.show_finestra_salvataggio_registrazione)
        self.timer2.timeout.connect(self.change_reg_lable)

    def change_reg_lable(self):
        self.ui.label_nome_reg_display.setText(self.banco_di_taratura.logger.path_CSV)

    def show_setup_window(self):
        self.setup_window.show()
        
    def show_graph_window(self):
        self.setup_graph.show()
        
    def show_finestra_salvataggio_registrazione(self):
        dname = QFileDialog.getExistingDirectory()
        if dname != '':
                self.banco_di_taratura.logger.path_directory_CSV = dname
                self.finestra_salvataggio_registrazione.exec()
        else:
                self.banco_di_taratura.error_window_logic("Path non selezionato!")
    
    def check(self):
        if self.timerStop == True:
            self.timer1.stop()
            self.timer2.stop()
        
    def setter_lcdDisplay_text_logger(self):
        self.logger.DATA.text_lcd[0]=self.ui.comboBox_1.currentText()
        self.logger.DATA.text_lcd[1]=self.ui.comboBox_2.currentText()
        self.logger.DATA.text_lcd[2]=self.ui.comboBox_3.currentText()
        self.logger.DATA.text_lcd[3]=self.ui.comboBox_4.currentText()
        self.logger.DATA.text_lcd_SG600_main_temp[0]=self.ui.comboBox_5.currentText()
    
    def pulsante_interfaccia_click(self):
        # Check della condizione del pulsante e poi cambio il tipo e gestisco il timer

        if self.status_pulsante_interfaccia % 2 != 0:
                self.timer1.start(100)          # In millisecondi
                self.ui.pushButton_Interfaccia.setText("STOP")
                self.ui.pushButton_Interfaccia.setStyleSheet("background-color: red; border-style: outset; border-width: 2px; border-color: black; color: black")
                self.ui.label.setStyleSheet("QWidget { background-color:rgb(255, 69, 72); border-style: outset; border-width: 0px; border-color:rgb(255, 111, 113); border-radius: 20px; } QLabel { color: rgb(0,0,0); }")
                self.ui.widget_sfond_interfaccia.setStyleSheet("QWidget { background-color:rgb(255, 69, 72); border-style: outset; border-width: 2px; border-color:rgb(255, 111, 113); border-radius: 20px; }")
                self.status_pulsante_interfaccia = self.status_pulsante_interfaccia + 1
        else:     
                self.timer1.stop()
                self.ui.lcdNumber_1.display(0)
                self.ui.lcdNumber_2.display(0)
                self.ui.lcdNumber_3.display(0)
                self.ui.lcdNumber_4.display(0)
                self.ui.lcdNumber_main_SG600.display(0)     
                self.ui.lcdNumber_temperature_SG600.display(0)      
                self.ui.pushButton_Interfaccia.setStyleSheet("background-color: green; border-style: outset; border-width: 2px; border-color: black; color: black")
                self.ui.label.setStyleSheet("QWidget { background-color:rgb(125, 225, 10); border-style: outset; border-width: 0px; border-color:rgb(63, 156, 23); border-radius: 20px; } QLabel { color: rgb(0,0,0); }")
                self.ui.widget_sfond_interfaccia.setStyleSheet("QWidget { background-color:rgb(125, 225, 10); border-style: outset; border-width: 2px; border-color:rgb(63, 156, 23); border-radius: 20px; }")
                self.ui.pushButton_Interfaccia.setText("START")
                self.status_pulsante_interfaccia = self.status_pulsante_interfaccia + 1
    
    def pulsante_registrazione_click(self):
        # Check della condizione del pulsante e poi cambio il tipo e gestisco il logger
        if self.status_pulsante_registrazione % 2 != 0: 
                self.ui.pushButton_setup_registrazione.setEnabled(False)
                if self.banco_di_taratura.registrazione_directory_path == None or self.banco_di_taratura.registrazione_name == None:
                        logging.error(f"Directory: {self.banco_di_taratura.registrazione_directory_path}, Name: {self.banco_di_taratura.registrazione_name}")
                        error_window = Error_window(banco_di_taratura=self.banco_di_taratura)
                        error_window.set_error_message(f"Il file per la registrazione non è stato definito.")
                        error_window.setWindowTitle("Error Window")
                        error_window.exec()
                else:
                        self.logger.DATA.startStop_logger = True
                        if self.logger.start_timer == None:
                                self.logger.start_timer = time.time()
                        self.ui.pushButton_Registrazione.setText("STOP")
                        self.ui.label_5.setStyleSheet("QWidget { background-color:rgb(255, 69, 72); border-style: outset; border-width: 0px; border-color:rgb(255, 111, 113); border-radius: 20px; } QLabel { color: rgb(0,0,0); }")
                        self.ui.pushButton_Registrazione.setStyleSheet("background-color: red; border-style: outset; border-width: 2px; border-color: black; color: black")
                        self.ui.widget_sfondo_registrazione.setStyleSheet("QWidget { background-color:rgb(255, 69, 72); border-style: outset; border-width: 2px; border-color:rgb(255, 111, 113); border-radius: 20px; }")
                        self.status_pulsante_registrazione = self.status_pulsante_registrazione + 1
        else:
                self.ui.pushButton_setup_registrazione.setEnabled(True)   
                self.logger.DATA.startStop_logger  = False     
                self.ui.pushButton_Registrazione.setText("START")     
                self.ui.label_5.setStyleSheet("QWidget { background-color:rgb(125, 225, 10); border-style: outset; border-width: 0px; border-color:rgb(63, 156, 23); border-radius: 20px; } QLabel { color: rgb(0,0,0); }")
                self.ui.pushButton_Registrazione.setStyleSheet("background-color: green; border-style: outset; border-width: 2px; border-color: black; color: black")
                self.ui.widget_sfondo_registrazione.setStyleSheet("QWidget { background-color:rgb(125, 225, 10); border-style: outset; border-width: 2px; border-color:rgb(63, 156, 23); border-radius: 20px; }")
                self.status_pulsante_registrazione = self.status_pulsante_registrazione + 1
                
           
           # "QWidget { background-color:rgb(255, 69, 72); border-style: outset; border-width: 2px; border-color:rgb(255, 111, 113); border-radius: 20px; }"
           
    def update_CH1(self):
        list_mV = self.controller_TCP.get_mv()
        list_Kg = self.controller_TCP.get_Kg()
        list_N = self.controller_TCP.get_N()
        list_Nm = self.controller_TCP.get_Nm()
        if self.ui.comboBox_1.currentText() == "mV":
                self.ui.lcdNumber_1.display(list_mV[0])
        elif self.ui.comboBox_1.currentText() == "Kg":
                self.ui.lcdNumber_1.display(list_Kg[0])
        elif self.ui.comboBox_1.currentText() == "N":
                self.ui.lcdNumber_1.display(list_N[0])
        elif self.ui.comboBox_1.currentText() == "Nm":
                self.ui.lcdNumber_1.display(list_Nm[0]) 
        else:
                print("Error: something went wrong in the selection of the measuring unit in CH1!")       
                exit(1)

    def update_CH2(self):
        list_mV = self.controller_TCP.get_mv()
        list_Kg = self.controller_TCP.get_Kg()
        list_N = self.controller_TCP.get_N()
        list_Nm = self.controller_TCP.get_Nm()
        if self.ui.comboBox_2.currentText() == "mV":
                self.ui.lcdNumber_2.display(list_mV[1])
        elif self.ui.comboBox_2.currentText() == "Kg":
                self.ui.lcdNumber_2.display(list_Kg[1])
        elif self.ui.comboBox_2.currentText() == "N":
                self.ui.lcdNumber_2.display(list_N[1])
        elif self.ui.comboBox_2.currentText() == "Nm":
                self.ui.lcdNumber_2.display(list_Nm[1]) 
        else:
                print("Error: something went wrong in the selection of the measuring unit in CH2!")       
                exit(1)


    def update_CH3(self):
        list_mV = self.controller_TCP.get_mv()
        list_Kg = self.controller_TCP.get_Kg()
        list_N = self.controller_TCP.get_N()
        list_Nm = self.controller_TCP.get_Nm()
        if self.ui.comboBox_3.currentText() == "mV":
                self.ui.lcdNumber_3.display(list_mV[2])
        elif self.ui.comboBox_3.currentText() == "Kg":
                self.ui.lcdNumber_3.display(list_Kg[2])
        elif self.ui.comboBox_3.currentText() == "N":
                self.ui.lcdNumber_3.display(list_N[2])
        elif self.ui.comboBox_3.currentText() == "Nm":
                self.ui.lcdNumber_3.display(list_Nm[2]) 
        else:
                print("Error: something went wrong in the selection of the measuring unit in CH3!")       
                exit(1)

    def update_CH4(self):
        list_mV = self.controller_TCP.get_mv()
        list_Kg = self.controller_TCP.get_Kg()
        list_N = self.controller_TCP.get_N()
        list_Nm = self.controller_TCP.get_Nm()
        if self.ui.comboBox_4.currentText() == "mV":
                self.ui.lcdNumber_4.display(list_mV[3])
        elif self.ui.comboBox_4.currentText() == "Kg":
                self.ui.lcdNumber_4.display(list_Kg[3])
        elif self.ui.comboBox_4.currentText() == "N":
                self.ui.lcdNumber_4.display(list_N[3])
        elif self.ui.comboBox_4.currentText() == "Nm":
                self.ui.lcdNumber_4.display(list_Nm[3]) 
        else:
                print("Error: something went wrong in the selection of the measuring unit in CH4!")       
                exit(1)
    
    
    def update_SG600_main(self):
        main_mV = self.controller_MODBUS.get_mV_main()
        main_Nm = self.controller_MODBUS.get_Nm_main()
        if self.ui.comboBox_5.currentText() == "mV":
                self.ui.lcdNumber_main_SG600.display(main_mV)
        elif self.ui.comboBox_5.currentText() == "Nm":
                self.ui.lcdNumber_main_SG600.display(main_Nm)
        else:
            print("Error: something went wrong in the selection of the measuring unit in SG600_main!")       
            exit(1)
                
                
    def update_SG600_temp(self):
        temp_C = self.controller_MODBUS.get_C_temp()
        self.ui.lcdNumber_temperature_SG600.display(temp_C)
        