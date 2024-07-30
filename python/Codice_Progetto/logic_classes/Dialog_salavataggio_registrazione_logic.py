from __future__ import annotations
from PySide6.QtWidgets import QDialog
from qt_classes.Dialog_salvataggio_ui import Ui_Dialog
import controller_classes.Logger as Logger
from typing import TYPE_CHECKING
import time

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from View_QT_HomePage_logic import MainWindow

""" Codice che gestisce la finestra nella quale si mette il nome del file di registrazione .csv """

class Salvataggio_registrazione(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, homepage:MainWindow):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_Dialog()
        # Setup the user interface (quindi tutti gli elementi saranno identificati da self.ui)
        self.ui.setupUi(self)
        # set modal per disabilitare le azioni dell' utente al di fuori della schermata
        self.setModal(True)
        self.homepage = homepage
        self.banco_di_taratura.registrazione_name = "Default"
        # set window icon serve per impostrae l'icona della finestra
        self.banco_di_taratura.set_window_icon(self)
        
        # segnali
        self.ui.pushButton_salvataggio.clicked.connect(self.update_filename)
        
        # Cambiamento titolo
        self.ui.label_salvataggio_title.setText("""<html><head/><body><p align="center"><span style=" font-size:16pt; color:#292fa3;">SALVATAGGIO FILE REGISTRAZIONE</span></p></body></html>""")

    # metodi
    def update_filename(self):
        
        """ aggiornamento dei dati in banco di taratura a seguito del salvataggio del .csv"""
        
        logger = Logger.LOGGER(nome_CSV=self.ui.lineEdit_nome_file.text(), banco_di_taratura=self.banco_di_taratura, path_directory_CSV=self.banco_di_taratura.logger.path_directory_CSV)
        self.banco_di_taratura.logger.path_CSV = logger.path_CSV  # Salvo il path completo
        self.banco_di_taratura.logger.nome_CSV = logger.nome_CSV  # Salvo solo il nome (senza .csv)
        self.banco_di_taratura.registrazione_directory_path = logger.path_directory_CSV  # Salvo il path della cartella in cui è salvato
        self.banco_di_taratura.registrazione_name = logger.nome_CSV  # Salvo solo il nome (senza .csv)
        self.banco_di_taratura.logger.start_timer = None  # istante iniziale usato per calcolare il tempo nella registrazione
        self.close()