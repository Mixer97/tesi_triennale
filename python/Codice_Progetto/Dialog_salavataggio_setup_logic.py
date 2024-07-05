from __future__ import annotations
from PySide6.QtWidgets import QDialog
from Dialog_salvataggio_ui import Ui_Dialog
from typing import TYPE_CHECKING
import Handler_JSON

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from View_QT_HomePage_logic import MainWindow

class Salvataggio_setup(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, homepage:MainWindow):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_Dialog()
        # Setup the user interface (quindi tutti gli elementi saranno identificati da self.ui)
        self.ui.setupUi(self)
        self.setModal(True)
        
        # segnali
        self.ui.lineEdit_nome_file.editingFinished.connect(self.update_filename)
        # self.ui.pushButton_salvataggio.clicked.connect(Handler_JSON.handle)
        
    # metodi
    def update_filename(self):
        self.banco_di_taratura.file_setup_name = self.ui.lineEdit_nome_file.text()
        self.close()