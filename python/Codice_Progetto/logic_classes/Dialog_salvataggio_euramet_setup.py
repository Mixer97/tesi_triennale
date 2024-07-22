from __future__ import annotations
from PySide6.QtWidgets import QDialog
from qt_classes.Dialog_salvataggio_ui import Ui_Dialog
from typing import TYPE_CHECKING
from logic_classes.Handler_JSON import handler_json

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from Dialog_xlxs_euramet_logic import csv_euramet_window

class Salvataggio_setup_euramet(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, euramet_setup_window:csv_euramet_window):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_Dialog()
        # Setup the user interface (quindi tutti gli elementi saranno identificati da self.ui)
        self.ui.setupUi(self)
        self.setModal(True)
        self.banco_di_taratura.file_setup_euramet_name = "Default"
        self.banco_di_taratura.set_window_icon(self)
        
        # segnali
        self.ui.lineEdit_nome_file.editingFinished.connect(self.update_filename)
        self.ui.pushButton_salvataggio.clicked.connect(self.save_setup)
        
    # metodi
    def update_filename(self):
        self.banco_di_taratura.file_setup_euramet_name = self.ui.lineEdit_nome_file.text()

        
    def save_setup(self):
        tmp = handler_json(nome_file_save=self.banco_di_taratura.file_setup_euramet_name, path_directory_save=self.banco_di_taratura.file_setup_euramet_directory_path)
        tmp.save_setup_euramet(banco_di_taratura=self.banco_di_taratura, setup_window_euramet=self)
        self.close()