from __future__ import annotations
from PySide6.QtWidgets import QDialog
from dialog_setup_SG600_ui import Ui_SG600_Setup
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
        coefficiente_main=self.controller_MODBUS.DATA.coefficiente_main
        coefficiente_temp=self.controller_MODBUS.DATA.coefficiente_temp
        m_main = self.banco_di_taratura.m_main
        q_main = self.banco_di_taratura.q_main
        m_temp = self.banco_di_taratura.m_temp
        q_temp = self.banco_di_taratura.q_temp
        self.ui.lineEdit_coefficiente_main.setText(str(coefficiente_main))
        self.ui.lineEdit_coefficiente_temp.setText(str(coefficiente_temp))
        self.ui.lineEdit_m_main.setText(str(m_main))
        self.ui.lineEdit_q_main.setText(str(q_main))
        self.ui.lineEdit_m_temp.setText(str(m_temp))
        self.ui.lineEdit_q_temp.setText(str(q_temp))
        
        # Setup dei segnali
        self.ui.lineEdit_coefficiente_main.editingFinished.connect(self.update_coefficiente_main)
        self.ui.lineEdit_coefficiente_temp.editingFinished.connect(self.update_coefficiente_temp)
        self.ui.lineEdit_m_main.editingFinished.connect(self.update_linear_correction_values)
        self.ui.lineEdit_q_main.editingFinished.connect(self.update_linear_correction_values)
        self.ui.lineEdit_m_temp.editingFinished.connect(self.update_linear_correction_values)
        self.ui.lineEdit_q_temp.editingFinished.connect(self.update_linear_correction_values)
        self.ui.pushButton_azzeramento_main.clicked.connect(self.update_zero_main)
        self.ui.pushButton_azzeramento_main_2.clicked.connect(self.update_zero_temp)

    def update_linear_correction_values(self):
        self.banco_di_taratura.m_main = float(self.ui.lineEdit_m_main.text())
        self.banco_di_taratura.q_main = float(self.ui.lineEdit_q_main.text())
        self.banco_di_taratura.m_temp = float(self.ui.lineEdit_m_temp.text())
        self.banco_di_taratura.q_temp = float(self.ui.lineEdit_q_temp.text())

    def update_zero_main(self):
        self.banco_di_taratura.controller_modbus.DATA.zero_main = self.banco_di_taratura.controller_modbus.DATA.canale_principale_mV

    def update_zero_temp(self):
        self.banco_di_taratura.controller_modbus.DATA.zero_temp = self.banco_di_taratura.controller_modbus.DATA.canale_temperatura_mV

    def update_coefficiente_main(self):
        new_value = float(self.ui.lineEdit_coefficiente_main.text())
        if is_number_tryexcept(new_value):
            self.controller_MODBUS.DATA.coefficiente_main = float(new_value)
        else:
            print("Valore inserito non rappresenta un numero")       

    def update_coefficiente_temp(self):
        new_value = float(self.ui.lineEdit_coefficiente_temp.text())
        if is_number_tryexcept(new_value):
            self.controller_MODBUS.DATA.coefficiente_temp = float(new_value)
        else:
            print("Valore inserito non rappresenta un numero")       


def is_number_tryexcept(s):
    """ Returns True if string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False