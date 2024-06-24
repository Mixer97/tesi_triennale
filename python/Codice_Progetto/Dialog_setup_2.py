from PySide6.QtWidgets import QDialog
from Dialog_setup_2_ui import Ui_Canale_Setup_2
from Banco_Taratura import BANCO_DI_TARATURA



class Canale_Setup_2(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_Canale_Setup_2()
        # Setup the user interface
        self.ui.setupUi(self)

        self.controller_TCP = banco_di_taratura.controller_tcp
        self.controller_MODBUS = banco_di_taratura.controller_modbus
        self.logger = banco_di_taratura.logger
        
 # Setup dei valori iniziali delle lineEdit
        i=self.controller_TCP.DATA.LIST_FULLSCALE[1]
        l=self.controller_TCP.DATA.LIST_SENSIBILITY[1]
        self.ui.lineEdit_fondoscala.setText(str(i))
        self.ui.lineEdit_sensibilita.setText(str(l))
        
        # Setup dei segnali
        self.ui.lineEdit_fondoscala.textChanged.connect(self.update_fondoscala)
        self.ui.lineEdit_sensibilita.textChanged.connect(self.update_sensibilità)

        
    def update_fondoscala(self):
        new_value = self.ui.lineEdit_fondoscala.text() 
        if is_number_tryexcept(new_value):
            self.controller_TCP.DATA.LIST_FULLSCALE[1] = float(new_value)
        else:
            print("Valore inserito non rappresenta un numero")       
            
    def update_sensibilità(self):
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