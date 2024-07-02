from __future__ import annotations
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow
from View_QT_HomePage_ui import Ui_MainWindow
from View_QT_SetupPage_logic import SetupWindow
from Mainwindow_grafico_logic import GraphWindow
from PySide6.QtCore import QSize
from typing import TYPE_CHECKING

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
        
        
        self.logger = banco_di_taratura.logger
        self.controller_TCP = banco_di_taratura.controller_tcp
        self.controller_MODBUS = banco_di_taratura.controller_modbus
        
        self.startStop = banco_di_taratura.startStop
        self.status_pulsante_interfaccia = banco_di_taratura.status_pulsante_interfaccia
        self.status_pulsante_registrazione = banco_di_taratura.status_pulsante_registrazione
        self.timerStop = banco_di_taratura.timerStop
        
        self.setup_window = SetupWindow(self.banco_di_taratura, self)
        self.setup_graph = GraphWindow(self.banco_di_taratura, self)
    
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
        self.pulsante_interfaccia_click()       # click iniziale per avviare l'interfaccia             
        self.timer1.timeout.connect(self.check)     # Check per chiusura dei timer alla chiusura dell'ultima finestra
        self.show_graph_window()         # Mostra il la finestra con il grafico all' apertura
        self.ui.pushButton_grafico.clicked.connect(self.show_graph_window)

    def show_setup_window(self):
        self.setup_window.show()
        
    def show_graph_window(self):
        self.setup_graph.show()
    
    def check(self):
        if self.timerStop == True:
            self.timer1.stop()
        #     self.timer2.stop()
        
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
                # self.timer2.start(100)          # In millisecondi       
                self.logger.DATA.startStop_logger = True
                self.ui.pushButton_Registrazione.setText("STOP")
                self.ui.label_5.setStyleSheet("QWidget { background-color:rgb(255, 69, 72); border-style: outset; border-width: 0px; border-color:rgb(255, 111, 113); border-radius: 20px; } QLabel { color: rgb(0,0,0); }")
                self.ui.pushButton_Registrazione.setStyleSheet("background-color: red; border-style: outset; border-width: 2px; border-color: black; color: black")
                self.ui.widget_sfondo_registrazione.setStyleSheet("QWidget { background-color:rgb(255, 69, 72); border-style: outset; border-width: 2px; border-color:rgb(255, 111, 113); border-radius: 20px; }")
                self.status_pulsante_registrazione = self.status_pulsante_registrazione + 1
        else:
                # self.timer2.stop()     
                self.logger.DATA.startStop_logger  = False     
                self.ui.pushButton_Registrazione.setText("START")     
                self.ui.label_5.setStyleSheet("QWidget { background-color:rgb(125, 225, 10); border-style: outset; border-width: 0px; border-color:rgb(63, 156, 23); border-radius: 20px; } QLabel { color: rgb(0,0,0); }")
                self.ui.pushButton_Registrazione.setStyleSheet("background-color: green; border-style: outset; border-width: 2px; border-color: black; color: black")
                self.ui.widget_sfondo_registrazione.setStyleSheet("QWidget { background-color:rgb(125, 225, 10); border-style: outset; border-width: 2px; border-color:rgb(63, 156, 23); border-radius: 20px; }")
                self.status_pulsante_registrazione = self.status_pulsante_registrazione + 1
                
           
           # "QWidget { background-color:rgb(255, 69, 72); border-style: outset; border-width: 2px; border-color:rgb(255, 111, 113); border-radius: 20px; }"
           
    def update_CH1(self):
        if self.ui.comboBox_1.currentText() == "mV":
                list_mV = self.controller_TCP.get_mv()
                self.ui.lcdNumber_1.display(list_mV[0])
        elif self.ui.comboBox_1.currentText() == "Kg":
                list_Kg = self.controller_TCP.get_Kg()
                self.ui.lcdNumber_1.display(list_Kg[0])
        elif self.ui.comboBox_1.currentText() == "N":
                list_N = self.controller_TCP.get_N()
                self.ui.lcdNumber_1.display(list_N[0])
        elif self.ui.comboBox_1.currentText() == "Nm":
                list_Nm = self.controller_TCP.get_Nm()
                self.ui.lcdNumber_1.display(list_Nm[0]) 
        else:
                print("Error: something went wrong in the selection of the measuring unit in CH1!")       
                exit(1)

    def update_CH2(self):
        if self.ui.comboBox_2.currentText() == "mV":
                list_mV = self.controller_TCP.get_mv()
                self.ui.lcdNumber_2.display(list_mV[1])
        elif self.ui.comboBox_2.currentText() == "Kg":
                list_Kg = self.controller_TCP.get_Kg()
                self.ui.lcdNumber_2.display(list_Kg[1])
        elif self.ui.comboBox_2.currentText() == "N":
                list_N = self.controller_TCP.get_N()
                self.ui.lcdNumber_2.display(list_N[1])
        elif self.ui.comboBox_2.currentText() == "Nm":
                list_Nm = self.controller_TCP.get_Nm()
                self.ui.lcdNumber_2.display(list_Nm[1]) 
        else:
                print("Error: something went wrong in the selection of the measuring unit in CH2!")       
                exit(1)


    def update_CH3(self):
        if self.ui.comboBox_3.currentText() == "mV":
                list_mV = self.controller_TCP.get_mv()
                self.ui.lcdNumber_3.display(list_mV[2])
        elif self.ui.comboBox_3.currentText() == "Kg":
                list_Kg = self.controller_TCP.get_Kg()
                self.ui.lcdNumber_3.display(list_Kg[2])
        elif self.ui.comboBox_3.currentText() == "N":
                list_N = self.controller_TCP.get_N()
                self.ui.lcdNumber_3.display(list_N[2])
        elif self.ui.comboBox_3.currentText() == "Nm":
                list_Nm = self.controller_TCP.get_Nm()
                self.ui.lcdNumber_3.display(list_Nm[2]) 
        else:
                print("Error: something went wrong in the selection of the measuring unit in CH3!")       
                exit(1)

    def update_CH4(self):
        if self.ui.comboBox_4.currentText() == "mV":
                list_mV = self.controller_TCP.get_mv()
                self.ui.lcdNumber_4.display(list_mV[3])
        elif self.ui.comboBox_4.currentText() == "Kg":
                list_Kg = self.controller_TCP.get_Kg()
                self.ui.lcdNumber_4.display(list_Kg[3])
        elif self.ui.comboBox_4.currentText() == "N":
                list_N = self.controller_TCP.get_N()
                self.ui.lcdNumber_4.display(list_N[3])
        elif self.ui.comboBox_4.currentText() == "Nm":
                list_Nm = self.controller_TCP.get_Nm()
                self.ui.lcdNumber_4.display(list_Nm[3]) 
        else:
                print("Error: something went wrong in the selection of the measuring unit in CH4!")       
                exit(1)
    
    
    def update_SG600_main(self):
        if self.ui.comboBox_5.currentText() == "mV":
                main_mV = self.controller_MODBUS.get_mV_main()
                self.ui.lcdNumber_main_SG600.display(main_mV)
        else:
            print("Error: something went wrong in the selection of the measuring unit in SG600_main!")       
            exit(1)
                
                
    def update_SG600_temp(self):
        temp_mV = self.controller_MODBUS.get_mV_temp()
        self.ui.lcdNumber_temperature_SG600.display(temp_mV)
        