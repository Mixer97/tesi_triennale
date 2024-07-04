from __future__ import annotations
from PySide6.QtWidgets import QDialog
from Dialog_setup_SG600_ui import Ui_SG600_Setup
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA



class Canale_Setup_SG600(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_SG600_Setup()
        # Setup the user interface
        self.ui.setupUi(self)
        self.setModal(True)
        
        self.controller_TCP = banco_di_taratura.controller_tcp
        self.controller_MODBUS = banco_di_taratura.controller_modbus
        self.logger = banco_di_taratura.logger


        
        # Setup dei valori iniziali delle lineEdit
        sens_main=self.controller_MODBUS.DATA.sensibilità_principale
        sens_temp=self.controller_MODBUS.DATA.sensibilità_temperatura
        full_main=self.controller_MODBUS.DATA.fondo_scala_principale
        full_temp=self.controller_MODBUS.DATA.fondo_scala_temperatura
        
        self.ui.lineEdit_fondoscala_main.setText(str(full_main))
        self.ui.lineEdit_sensibilita_main.setText(str(sens_main))
        self.ui.lineEdit_fondoscala_temp.setText(str(full_temp))
        self.ui.lineEdit_sensibilita_temp.setText(str(sens_temp))
        
        # Setup dei segnali
        self.ui.lineEdit_fondoscala_main.textChanged.connect(self.update_fondoscala_main)
        self.ui.lineEdit_sensibilita_main.textChanged.connect(self.update_sensibilità_main)
        self.ui.lineEdit_fondoscala_temp.textChanged.connect(self.update_fondoscala_temp)
        self.ui.lineEdit_sensibilita_temp.textChanged.connect(self.update_sensibilità_temp)
        self.ui.pushButton_azzeramento_main.clicked.connect(self.update_zero_main)
        self.ui.pushButton_azzeramento_main_2.clicked.connect(self.update_zero_temp)


    def update_zero_main(self):
        self.banco_di_taratura.controller_modbus.DATA.zero_main = self.banco_di_taratura.controller_modbus.DATA.canale_principale_mV


    def update_zero_temp(self):
        self.banco_di_taratura.controller_modbus.DATA.zero_temp = self.banco_di_taratura.controller_modbus.DATA.canale_temperatura_mV

        
    def update_fondoscala_main(self):
        new_value = self.ui.lineEdit_fondoscala_main.text() 
        if is_number_tryexcept(new_value):
            self.controller_MODBUS.DATA.fondo_scala_principale = float(new_value)
        else:
            print("Valore inserito non rappresenta un numero")       
            
    def update_sensibilità_main(self):
        new_value = self.ui.lineEdit_sensibilita_main.text() 
        if is_number_tryexcept(new_value):
            self.controller_MODBUS.DATA.sensibilità_principale = float(new_value)
        else:
            print("Valore inserito non rappresenta un numero")
            
    def update_fondoscala_temp(self):
        new_value = self.ui.lineEdit_fondoscala_temp.text() 
        if is_number_tryexcept(new_value):
            self.controller_MODBUS.DATA.fondo_scala_temperatura = float(new_value)
        else:
            print("Valore inserito non rappresenta un numero")       
            
    def update_sensibilità_temp(self):
        new_value = self.ui.lineEdit_sensibilita_temp.text() 
        if is_number_tryexcept(new_value):
            self.controller_MODBUS.DATA.sensibilità_temperatura = float(new_value)
        else:
            print("Valore inserito non rappresenta un numero")


def is_number_tryexcept(s):
    """ Returns True if string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False