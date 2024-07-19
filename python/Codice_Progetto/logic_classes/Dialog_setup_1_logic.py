from __future__ import annotations
from PySide6.QtWidgets import QDialog
from qt_classes.Dialog_setup_1_ui import Ui_Canale_Setup_1
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA


class Canale_Setup_1(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_Canale_Setup_1()
        # Setup the user interface (quindi tutti gli elementi saranno identificati da self.ui)
        self.ui.setupUi(self)
        self.setModal(True)
        self.ui.pushButton_azzeramento_tara.setStyleSheet(
            """
QWidget{
    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.965909, stop:0 rgba(255, 220, 129, 236), stop:1 rgba(255, 110, 110, 242)); 
    border-style: outset;
    border-width: 2px;
    border-color: rgb(255, 106, 0);
    border-radius: 20px;
    color: rgb(0,0,0);
}
QPushButton::pressed{
    border-width: 2px;
    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.965909, stop:0 rgba(255, 110, 110, 242), stop:1 rgba(255, 220, 129, 236)); 
    color: rgb(0, 0, 0);
}
"""
        )
        
        self.controller_TCP = banco_di_taratura.controller_tcp
        self.controller_MODBUS = banco_di_taratura.controller_modbus
        self.logger = banco_di_taratura.logger
        
        # Setup dei valori iniziali delle lineEdit
        i=self.controller_TCP.DATA.LIST_FULLSCALE[0]
        l=self.controller_TCP.DATA.LIST_SENSIBILITY[0]
        self.ui.lineEdit_fondoscala.setText(str(i))
        self.ui.lineEdit_sensibilita.setText(str(l))

        
        # Setup dei segnali
        # self.lineEdit_fondoscala
        self.ui.lineEdit_fondoscala.textChanged.connect(self.update_fondoscala)
        self.ui.lineEdit_sensibilita.textChanged.connect(self.update_sensibilità)
        self.ui.pushButton_azzeramento_tara.clicked.connect(self.update_zero)


    def update_zero(self):
        self.banco_di_taratura.controller_tcp.DATA.LIST_mV_ZERO[0] = self.banco_di_taratura.controller_tcp.DATA.LIST_mV_VALUE[0]
        
    def update_fondoscala(self):
        new_value = self.ui.lineEdit_fondoscala.text() 
        if is_number_tryexcept(new_value):
            self.controller_TCP.DATA.LIST_FULLSCALE[0] = float(new_value)
        else:
            print("Valore inserito non rappresenta un numero")       
            
    def update_sensibilità(self):
        new_value = self.ui.lineEdit_sensibilita.text() 
        if is_number_tryexcept(new_value):
            self.controller_TCP.DATA.LIST_SENSIBILITY[0] = float(new_value)
        else:
            print("Valore inserito non rappresenta un numero")
            
def is_number_tryexcept(s):
    """ Returns True if string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False