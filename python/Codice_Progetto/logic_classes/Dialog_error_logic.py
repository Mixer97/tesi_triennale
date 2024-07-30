from __future__ import annotations
from PySide6.QtWidgets import QDialog
from qt_classes.Dialog_error_ui import Ui_Dialog_Error
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    
""" Codice per gestire la creazione della finestra di errore che viene usata dalle altre parti di codice """

class Error_window(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_Dialog_Error()
        # Setup the user interface (quindi tutti gli elementi saranno identificati da self.ui)
        self.ui.setupUi(self)
        self.setModal(True)
        
        # segnali
        self.ui.pushButton_error.clicked.connect(self.close)
        
    def set_error_message(self, message):
        self.ui.label_Error.setText(message)
        
        """Implementazione della finestra di errore"""
        """
        error_window = Error_window(banco_di_taratura=self.banco_di_taratura)
        error_window.set_error_message("Errore nella selezione del file (file selezionato non è json)")
        error_window.setWindowTitle("Error Window")
        error_window.exec()
        """
        """--------------------------------------------"""