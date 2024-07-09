from __future__ import annotations
from PySide6.QtWidgets import QDialog
from Dialog_setup_euramet_ui import Ui_Dialog_Euramet_setup
from Dialog_csv_euramet_logic import csv_euramet_window
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA



class Euramet_window(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_Dialog_Euramet_setup()
        # Setup the user interface
        self.ui.setupUi(self)
        
        
        self.list_status_checkbox = self.banco_di_taratura.list_status_checkbox_euramet_page  #[salita_1, discesa_1, salita_2]
        self.current_number_of_steps = self.banco_di_taratura.current_number_of_steps  #[default: 5]
        self.status_inserimento_altezza = self.banco_di_taratura.status_inserimento_altezza  #[defualt: True]
        
        # segnali
        self.ui.comboBox_step.currentIndexChanged.connect(self.update_steps)
        self.ui.checkBox_altezza.stateChanged.connect(self.update_altezza_state)
        self.ui.checkBox_salita_1.stateChanged.connect(self.update_status_salita_1)
        self.ui.checkBox_discesa_1.stateChanged.connect(self.update_status_discesa_1)
        self.ui.checkBox_salita_2.stateChanged.connect(self.update_status_salita_2)
        self.ui.pushButton_impostazion_csv.clicked.connect(self.show_csv_setup_window)
        
    def show_csv_setup_window(self):
        csv_setup_window = csv_euramet_window(self.banco_di_taratura, self)
        csv_setup_window.exec()
        
    def update_steps(self):
        self.current_number_of_steps = self.ui.comboBox_step.currentIndex() + 1   # index da 0 a 4 e io voglio da 1 a 5
        
    def update_altezza_state(self):
        self.status_inserimento_altezza = self.ui.checkBox_altezza.isChecked() 
        
    def update_status_salita_1(self):
        tmp = self.ui.checkBox_salita_1.isChecked()
        if tmp:
            self.list_status_checkbox[0] = 1
        else:
            self.list_status_checkbox[0] = 0
        print(self.list_status_checkbox)
        
    def update_status_discesa_1(self):
        tmp = self.ui.checkBox_discesa_1.isChecked()
        if tmp:
            self.list_status_checkbox[1] = 1
        else:
            self.list_status_checkbox[1] = 0
        print(self.list_status_checkbox)
            
    def update_status_salita_2(self):
        tmp = self.ui.checkBox_salita_2.isChecked()
        if tmp:
            self.list_status_checkbox[2] = 1
        else:
            self.list_status_checkbox[2] = 0
        print(self.list_status_checkbox)