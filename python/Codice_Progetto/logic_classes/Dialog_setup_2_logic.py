from __future__ import annotations
from PySide6.QtWidgets import QDialog
from qt_classes.dialog_setup_template_ui import Ui_Canale_Setup
from PySide6.QtCore import QCoreApplication
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from View_QT_SetupPage_logic import SetupWindow



class Canale_Setup_2(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, setup_window:SetupWindow):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        self.setup_window = setup_window
        # Create an instance of the generated UI class
        self.ui = Ui_Canale_Setup()
        # Setup the user interface
        self.setWindowTitle(QCoreApplication.translate("Canale_Setup_2", u"Channel_2 Setup Window", None))
        self.banco_di_taratura.set_window_icon(self)
        self.ui.setupUi(self)
        self.ui.comboBox_fullscale.removeItem(2)  # Rimuovo la possibilità di scegliere "Nm"
        self.ui.label_setup_title.setText("""<html><head/><body><p align="center"><span style=" font-size:20pt; font-weight:700; color:#00aa00;">CELLA DI CARICO</span></p></body></html>""")

        self.controller_TCP = banco_di_taratura.controller_tcp
        self.controller_MODBUS = banco_di_taratura.controller_modbus
        self.logger = banco_di_taratura.logger
        self.setModal(True)
        self.setWindowTitle("CANALE 2 SETUP")
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
        
 # Setup dei valori iniziali delle lineEdit
        i=self.controller_TCP.DATA.LIST_FULLSCALE[1]/9.81  # Siccome il fondoscala è gestito sempre in N e il valore iniziale è visualizzato in Kg dal menu a tendina
        l=self.controller_TCP.DATA.LIST_SENSIBILITY[1]
        self.ui.lineEdit_fondoscala.setText(str(i))
        self.ui.lineEdit_sensibilita.setText(str(l))
        
        # Setup dei segnali
        self.ui.lineEdit_fondoscala.textChanged.connect(self.update_fondoscala)
        self.ui.lineEdit_sensibilita.textChanged.connect(self.update_sensibilità)
        self.ui.pushButton_azzeramento_tara.clicked.connect(self.update_zero)


    def update_zero(self):
        """Salva lo zero in mV del canale"""
        self.banco_di_taratura.controller_tcp.DATA.LIST_mV_ZERO[1] = self.banco_di_taratura.controller_tcp.DATA.LIST_mV_VALUE[1]

        
    def update_fondoscala(self):
        """Salva il fondoscala del canale"""
        new_value = self.ui.lineEdit_fondoscala.text() 
        if is_number_tryexcept(new_value):
            if self.ui.comboBox_fullscale.currentText()=="Kg":
                self.controller_TCP.DATA.LIST_FULLSCALE[1] = float(new_value)*9.81
            elif self.ui.comboBox_fullscale.currentText()=="N":
                self.controller_TCP.DATA.LIST_FULLSCALE[1] = float(new_value)
        else:
            print("Valore inserito non rappresenta un numero")       
            
    def update_sensibilità(self):
        """Salva la sensibilità del canale"""
        new_value = self.ui.lineEdit_sensibilita.text() 
        if is_number_tryexcept(new_value):
            self.controller_TCP.DATA.LIST_SENSIBILITY[1] = float(new_value)
        else:
            print("Valore inserito non rappresenta un numero")
    
    
def is_number_tryexcept(s):
    """ Returns True if string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False