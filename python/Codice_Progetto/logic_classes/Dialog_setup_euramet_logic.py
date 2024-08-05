from __future__ import annotations
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QTimer
from PySide6.QtCore import QCoreApplication
from qt_classes.Dialog_setup_euramet_ui import Ui_Dialog_Euramet_setup
from logic_classes.Dialog_xlxs_euramet_logic import csv_euramet_window
from typing import TYPE_CHECKING
from openpyxl import load_workbook
from logic_classes.Euramet_logic import Misura_euramet
from logic_classes.Dialog_error_logic import Error_window
import logging

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from Mainwindow_grafico_logic import GraphWindow



class Euramet_window(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, graph_window:GraphWindow):
        """
        VARIABILI USATE IN BANCO DI TARATURA
        
        self.banco_di_taratura.list_status_checkbox_euramet_page     [salita_1, discesa_1, salita_2]
        self.banco_di_taratura.current_number_of_steps               [default: 5]
        self.banco_di_taratura.status_inserimento_altezza            [defualt: True]
        """
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        self.graph_window = graph_window
        # Create an instance of the generated UI class
        self.ui = Ui_Dialog_Euramet_setup()
        # Setup the user interface
        self.setWindowTitle(QCoreApplication.translate("Euramet_window", u"Euramet Window", None))
        self.banco_di_taratura.set_window_icon(self)
        self.ui.setupUi(self)
        
        self.csv_setup_window = csv_euramet_window(self.banco_di_taratura, self)
        self.csv_setup_window.setWindowTitle("Euramet Setup Window")
        
        # self.timer_update = QTimer()
        # self.timer_update.setInterval(100)
        # self.timer_update.timeout.connect(self.update_combobox)
        # self.timer_update.start()
        
        self.ui.comboBox_step.setCurrentIndex(3)  # Posiziono con 5 step di default
        self.ui.stackedWidget_euramet.setCurrentIndex(3)  # Posiziono con 5 step di default
        
        # segnali
        self.ui.comboBox_step.currentIndexChanged.connect(self.update_steps) # cambia gli step nel programma quando varian l'indice della combobox
        self.ui.checkBox_altezza.stateChanged.connect(self.update_altezza_state)
        self.ui.checkBox_salita_1.stateChanged.connect(self.update_status_salita_1)
        self.ui.checkBox_discesa_1.stateChanged.connect(self.update_status_discesa_1)
        self.ui.checkBox_salita_2.stateChanged.connect(self.update_status_salita_2)

        self.ui.pushButton_impostazioni_csv.clicked.connect(self.show_csv_setup_window)
        self.ui.comboBox_quadrante.currentIndexChanged.connect(self.update_quadrant)
        self.ui.comboBox_step.currentIndexChanged.connect(self.ui.stackedWidget_euramet.setCurrentIndex) # Varia la visualizzazione
        self.ui.pushButton_concludi_setup.clicked.connect(self.end_setup)
        
        self.ui.horizontalSlider_stabilita_giallo.sliderReleased.connect(self.update_valori_sliders)  # segnali per acuisire il valore degli sliders
        self.ui.horizontalSlider_stabilita_verde.sliderReleased.connect(self.update_valori_sliders)
        self.ui.horizontalSlider_varianza_giallo.sliderReleased.connect(self.update_valori_sliders)
        self.ui.horizontalSlider_varianza_verde.sliderReleased.connect(self.update_valori_sliders)


    # usato per inizializzare il secondo quadrante e terminare alla fine del 2 quadrante
    def change_quadrant(self):
        """
        Viene chiamato ogni volta che finisce la misura sullo zero finale della salita 2
        
        Inizia con quadrant_counter = 0
        
        Quando finisco il primo quadrante ho quadrant_counter = 1 e inverto i quadranti
        
        Quando finisco il secondo quadrante ho quadrant_counter = 2 e concludo Euramet
        
        """
        if self.banco_di_taratura.quadrant_counter == 1:
            self.invert_quadrant()
            self.graph_window.euramet_measure_entity = Misura_euramet(banco_di_taratura=self.banco_di_taratura, graphwindow=self.graph_window, euramet_window=self)    
        elif self.banco_di_taratura.quadrant_counter == 2:
            print("Euramet_finito!")
            self.graph_window.ui.pushButton_save_measure.setEnabled(False)
            self.graph_window.ui.label_step_attuale_valore.setText("#######")
            self.invert_quadrant()
            self.graph_window.euramet_measure_entity = Misura_euramet(banco_di_taratura=self.banco_di_taratura, graphwindow=self.graph_window, euramet_window=self)
            self.banco_di_taratura.quadrant_counter = 0
            self.graph_window.ui.graphWidget_visual_euramet.clear()
            self.graph_window.ui.label_step_prossimo_valore.setText("#######")
            self.graph_window.euramet_measure_entity = None
            self.graph_window.stability_logic()
        else:
            logging.error(f"La logica di change_quadrant NON deve arrivare qui! quadrant_counter={self.banco_di_taratura.quadrant_counter}")
    
    def update_combobox(self):
        
        if self.banco_di_taratura.list_status_checkbox_euramet_page[0]==0:
            self.ui.checkBox_salita_1.setChecked(False)
        else:
            self.ui.checkBox_salita_1.setChecked(True)
            
        if self.banco_di_taratura.list_status_checkbox_euramet_page[1]==0:
            self.ui.checkBox_discesa_1.setChecked(False)
        else:
            self.ui.checkBox_discesa_1.setChecked(True)
            
        if self.banco_di_taratura.list_status_checkbox_euramet_page[2]==0:
            self.ui.checkBox_salita_2.setChecked(False)
        else:
            self.ui.checkBox_salita_2.setChecked(True)
            
        if self.banco_di_taratura.status_inserimento_altezza:
            self.ui.checkBox_altezza.setChecked(True)
        else:
            self.ui.checkBox_altezza.setChecked(False)   
        
    def invert_quadrant(self):
        """
        Inverte il Q1 con il Q3 o viceversa
        """
        if self.banco_di_taratura.quadrant == "Q1":
            self.banco_di_taratura.quadrant = "Q3"
            self.graph_window.ui.label_quadrante.setText("Q3")
        elif self.banco_di_taratura.quadrant == "Q3":
            self.banco_di_taratura.quadrant = "Q1"
            self.graph_window.ui.label_quadrante.setText("Q1")
        else:
            print("Error nel valore del quadrante attuale")
            
    def show_csv_setup_window(self):
        self.csv_setup_window.exec()
        
    def end_setup(self):
        """
        Controlla che il path dell' excell esista, se esiste:
        
        Resetta logic_flip_flop a True e quadrant_counter a 0, poi carica il file excell già creato e inizializza Misura_euramet
        
        """
        if self.banco_di_taratura.excell_full_path == None:
            error_window = Error_window(banco_di_taratura=self.banco_di_taratura)
            error_window.set_error_message(f"Il file per Euramet non è stato definito.")
            error_window.setWindowTitle("Error Window")
            error_window.exec()
        else:
            self.graph_window.stability_logic()
            self.graph_window.logic_flip_flop = True
            self.banco_di_taratura.quadrant_counter = 0
            self.banco_di_taratura.quadrant = self.ui.comboBox_quadrante.currentText()
            self.banco_di_taratura.workbook = load_workbook(self.banco_di_taratura.excell_full_path)
            self.graph_window.ui.pushButton_save_measure.setEnabled(True)
            self.graph_window.ui.label_quadrante.setText(self.banco_di_taratura.quadrant)
            self.graph_window.ui.label_step_attuale_valore.setText("0 Nm")
            self.graph_window.euramet_measure_entity = Misura_euramet(banco_di_taratura=self.banco_di_taratura, graphwindow=self.graph_window, euramet_window=self)
            if self.banco_di_taratura.status_inserimento_altezza == False:
                self.graph_window.ui.frame_altezza.setEnabled(False)
            self.graph_window.show()
            self.close()
        
    def update_steps(self):
        self.banco_di_taratura.current_number_of_steps = self.ui.comboBox_step.currentIndex() + 2   # index da 0 a 3 e io voglio da 2 a 5
        self.csv_setup_window.update_steps()
    
    def update_quadrant(self):
        self.banco_di_taratura.quadrant = f"{self.ui.comboBox_quadrante.currentText()}"
        print(self.banco_di_taratura.quadrant)
        
    def update_altezza_state(self):
        tmp = self.ui.checkBox_altezza.isChecked()
        if tmp:
            self.banco_di_taratura.status_inserimento_altezza = True
        else:
            self.banco_di_taratura.status_inserimento_altezza = False
        print(self.banco_di_taratura.list_status_checkbox_euramet_page)
        
    def update_valori_sliders(self):
        self.banco_di_taratura.percentage_interval_green = self.ui.horizontalSlider_stabilita_verde.value()
        self.banco_di_taratura.percentage_interval_yellow = self.ui.horizontalSlider_stabilita_giallo.value()
        self.banco_di_taratura.difference_variance_green = self.ui.horizontalSlider_varianza_verde.value()
        self.banco_di_taratura.difference_variance_yellow = self.ui.horizontalSlider_varianza_giallo.value()
        
        self.ui.label_stabilit_verde.setText(f"{self.banco_di_taratura.percentage_interval_green}%")
        self.ui.label_stabilita_giallo.setText(f"{self.banco_di_taratura.percentage_interval_yellow}%")
        self.ui.label_varianza_verde.setText(f"{self.banco_di_taratura.difference_variance_green}")
        self.ui.label_varianza_giallo.setText(f"{self.banco_di_taratura.difference_variance_yellow}")
        
    def update_status_salita_1(self):
        tmp = self.ui.checkBox_salita_1.isChecked()
        if tmp:
            self.banco_di_taratura.list_status_checkbox_euramet_page[0] = 1
        else:
            self.banco_di_taratura.list_status_checkbox_euramet_page[0] = 0
        print(self.banco_di_taratura.list_status_checkbox_euramet_page)
        
    def update_status_discesa_1(self):
        tmp = self.ui.checkBox_discesa_1.isChecked()
        if tmp:
            self.banco_di_taratura.list_status_checkbox_euramet_page[1] = 1
        else:
            self.banco_di_taratura.list_status_checkbox_euramet_page[1] = 0
        print(self.banco_di_taratura.list_status_checkbox_euramet_page)
            
    def update_status_salita_2(self):
        tmp = self.ui.checkBox_salita_2.isChecked()
        if tmp:
            self.banco_di_taratura.list_status_checkbox_euramet_page[2] = 1
        else:
            self.banco_di_taratura.list_status_checkbox_euramet_page[2] = 0
        print(self.banco_di_taratura.list_status_checkbox_euramet_page)