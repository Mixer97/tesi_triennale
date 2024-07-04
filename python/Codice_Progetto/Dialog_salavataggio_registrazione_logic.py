from __future__ import annotations
from PySide6.QtWidgets import QDialog
from Dialog_salvataggio_ui import Ui_Dialog
from typing import TYPE_CHECKING
import Handler_CSV

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA


class Salvataggio_registrazione(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_Dialog()
        # Setup the user interface (quindi tutti gli elementi saranno identificati da self.ui)
        self.ui.setupUi(self)
        self.setModal(True)
        
        # segnali
        self.ui.lineEdit_nome_file.editingFinished.connect(self.update_filename)
        self.ui.pushButton_salvataggio.clicked.connect(Handler_CSV.handle)
        
        # Cambiamenti
        self.ui.label_salvataggio_title.setText("SALVATAGGIO FILE REGISTRAZIONE")
        self.ui.pushButton_salvataggio.setText("CAMBIA NOME")
        
    # metodi
    def update_filename(self):
        self.banco_di_taratura.file_csv_name = self.ui.lineEdit_nome_file.text()