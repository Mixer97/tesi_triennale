from __future__ import annotations
from PySide6.QtWidgets import QDialog
from qt_classes.Dialog_salvataggio_ui import Ui_Dialog
import controller_classes.Logger as Logger
from typing import TYPE_CHECKING
import time

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from View_QT_HomePage_logic import MainWindow

class Salvataggio_registrazione(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, homepage:MainWindow):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_Dialog()
        # Setup the user interface (quindi tutti gli elementi saranno identificati da self.ui)
        self.ui.setupUi(self)
        self.setModal(True)
        self.homepage = homepage
        self.banco_di_taratura.registrazione_name = "Default"
        self.banco_di_taratura.set_window_icon(self)
        
        # segnali
        # self.ui.lineEdit_nome_file.editingFinished.connect(self.update_filename)
        self.ui.pushButton_salvataggio.clicked.connect(self.update_filename)
        
        # Cambiamenti
        self.ui.label_salvataggio_title.setText("""<html><head/><body><p align="center"><span style=" font-size:16pt; color:#292fa3;">SALVATAGGIO FILE REGISTRAZIONE</span></p></body></html>""")

    # metodi
    def update_filename(self):
        
        logger = Logger.LOGGER(nome_CSV=self.ui.lineEdit_nome_file.text(), banco_di_taratura=self.banco_di_taratura, path_directory_CSV=self.banco_di_taratura.logger.path_directory_CSV)
        self.banco_di_taratura.logger.path_CSV = logger.path_CSV
        self.banco_di_taratura.logger.nome_CSV = logger.nome_CSV
        self.banco_di_taratura.logger.start_timer = None
        self.close()
        # self.banco_di_taratura.logger = Logger.LOGGER(nome_CSV=self.ui.lineEdit_nome_file.text(), banco_di_taratura=self.banco_di_taratura)
        # self.banco_di_taratura.logger.check_path()