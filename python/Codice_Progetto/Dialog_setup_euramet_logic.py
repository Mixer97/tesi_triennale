from __future__ import annotations
from PySide6.QtWidgets import QDialog
from Dialog_setup_euramet_ui import Ui_Dialog_Euramet_setup
from Dialog_csv_euramet_logic import csv_euramet_window
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from Mainwindow_grafico_logic import GraphWindow



class Euramet_window(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, graph_window:GraphWindow):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_Dialog_Euramet_setup()
        # Setup the user interface
        self.ui.setupUi(self)
        self.csv_setup_window = csv_euramet_window(self.banco_di_taratura, self)
        self.graph_window = graph_window
        
        """
        VARIABILI USATE IN BANCO DI TARATURA
        self.banco_di_taratura.list_status_checkbox_euramet_page     [salita_1, discesa_1, salita_2]
        self.banco_di_taratura.current_number_of_steps               [default: 5]
        self.banco_di_taratura.status_inserimento_altezza            [defualt: True]
        """
        
        self.ui.comboBox_step.setCurrentIndex(4)  # Posiziono con 5 step di default
        self.ui.stackedWidget_euramet.setCurrentIndex(4)  # Posiziono con 5 step di default
        
        # segnali
        self.ui.comboBox_step.currentIndexChanged.connect(self.update_steps)
        self.ui.checkBox_altezza.stateChanged.connect(self.update_altezza_state)
        self.ui.checkBox_salita_1.stateChanged.connect(self.update_status_salita_1)
        self.ui.checkBox_discesa_1.stateChanged.connect(self.update_status_discesa_1)
        self.ui.checkBox_salita_2.stateChanged.connect(self.update_status_salita_2)
        self.ui.pushButton_impostazion_csv.clicked.connect(self.show_csv_setup_window)
        self.ui.comboBox_step.currentIndexChanged.connect(self.ui.stackedWidget_euramet.setCurrentIndex)
        self.ui.pushButton_concludi_setup.clicked.connect(self.end_setup)
        self.ui.comboBox_quadrante.currentIndexChanged.connect(self.update_quadrant)
        
    def show_csv_setup_window(self):
        self.csv_setup_window.exec()
        
    def end_setup(self):
        self.graph_window.show()
        self.close()
        
    def update_steps(self):
        self.banco_di_taratura.current_number_of_steps = self.ui.comboBox_step.currentIndex() + 1   # index da 0 a 4 e io voglio da 1 a 5
        self.csv_setup_window.update_steps()
    
    def update_quadrant(self):
        self.banco_di_taratura.quadrant = f"{self.ui.comboBox_quadrante.currentText()}"
        print(self.banco_di_taratura.quadrant)
        
    def update_altezza_state(self):
        self.status_inserimento_altezza = self.ui.checkBox_altezza.isChecked() 
        
    def update_status_salita_1(self):
        tmp = self.ui.checkBox_salita_1.isChecked()
        if tmp:
            self.banco_di_taratura.list_status_checkbox_euramet_page[0] = 1
        else:
            self.banco_di_taratura.list_status_checkbox_euramet_page[0] = 0
        print(self.banco_di_taratura.list_status_checkbox_euramet_page)
        
    def update_status_discesa_1(self):
        tmp = self.ui.checkBox_discesa_1.isChecked()
        if tmp:
            self.banco_di_taratura.list_status_checkbox_euramet_page[1] = 1
        else:
            self.banco_di_taratura.list_status_checkbox_euramet_page[1] = 0
        print(self.banco_di_taratura.list_status_checkbox_euramet_page)
            
    def update_status_salita_2(self):
        tmp = self.ui.checkBox_salita_2.isChecked()
        if tmp:
            self.banco_di_taratura.list_status_checkbox_euramet_page[2] = 1
        else:
            self.banco_di_taratura.list_status_checkbox_euramet_page[2] = 0
        print(self.banco_di_taratura.list_status_checkbox_euramet_page)