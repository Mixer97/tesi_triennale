from __future__ import annotations
from PySide6.QtWidgets import QDialog
from Dialog_xlxs_euramet_ui import Ui_Dialog_csv_euramet
from typing import TYPE_CHECKING
from openpyxl import load_workbook
from Dialog_error_logic import Error_window
import os

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from Dialog_setup_euramet_logic import Euramet_window

class csv_euramet_window(QDialog):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, euramet_window:Euramet_window):
        super().__init__()
        self.banco_di_taratura=banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_Dialog_csv_euramet()
        # Setup the user interface (quindi tutti gli elementi saranno identificati da self.ui)
        self.ui.setupUi(self)
        self.setModal(True)
        self.euramet_window = euramet_window
        self.ui.lineEdit_scale.setText(f"{self.banco_di_taratura.controller_modbus.DATA.coefficiente_main}")
        self.counter_registrazione = 0
        self.tmp = None
        
    # segnali
        self.ui.pushButton_save_and_back.clicked.connect(self.save_and_back)
        
    def save_and_back(self):
        self.save_process()
        self.update_steps()
        self.euramet_window.show()
        self.close()
        
    def save_process(self):
        
        # due celle di partenza per Q1 e Q3
        self.colonna_start_Q1 = str(self.ui.label_colonna_start_Q1.text())
        self.colonna_start_Q3 = str(self.ui.label_colonna_start_Q3.text())
        self.riga_start_Q1 = int(self.ui.label_riga_start_Q1.text())
        self.riga_start_Q3 = int(self.ui.label_riga_start_Q3.text())
        self.banco_di_taratura.euramet_cella_inizio_precarichi_Q1 = self.format_to_list(self.colonna_start_Q1, self.riga_start_Q1)
        self.banco_di_taratura.euramet_cella_inizio_precarichi_Q3 = self.format_to_list(self.colonna_start_Q3, self.riga_start_Q3)
        
        # dati per il file excell
        self.banco_di_taratura.euramet_unita_ingegneristica_di_misura = self.ui.lineEdit_unita_ingegneristica_di_misura.text()
        self.banco_di_taratura.euramet_Unità_ingegneristica_UUT = self.ui.lineEdit_unita_ingegneristica_UUT.text()
        self.banco_di_taratura.controller_modbus.DATA.coefficiente_main = int(self.ui.lineEdit_scale.text())
        self.banco_di_taratura.euramet_Offset = float(self.ui.lineEdit_offset.text())
        self.banco_di_taratura.euramet_Coppia_taratura_MAX = int(self.ui.lineEdit_coppia_taratura_max.text())
        self.banco_di_taratura.euramet_Data = self.ui.lineEdit_data.text()
        self.banco_di_taratura.euramet_Rif_interno_attivita = self.ui.lineEdit_rif_interno_attivita.text()
        self.banco_di_taratura.euramet_Cliente = self.ui.lineEdit_cliente.text()
        self.banco_di_taratura.euramet_SN_TX = self.ui.lineEdit_SN_TX.text()
        self.banco_di_taratura.euramet_Descrizione_UUT = self.ui.lineEdit_descrizione_UUT.text()
        self.banco_di_taratura.euramet_Progetto_UUT = self.ui.lineEdit_progetto_UUT.text()
        self.banco_di_taratura.euramet_SN_UUT = self.ui.lineEdit_SN_UUT.text()
        self.banco_di_taratura.euramet_Report_di_calibrazione_TX = self.ui.lineEdit_report_calibrazione_TX.text()
        
        self.banco_di_taratura.excell_page_data = str(self.ui.label_nome_foglio_dati.text())
        self.banco_di_taratura.excell_name = str(self.ui.label_nome_excell.text())
        
        # apro e salvo in un excell copia i dati
        self.workbook = load_workbook(self.banco_di_taratura.excell_path_template)
        sheet_euramet = self.workbook["Istruzioni Uso"]

        sheet_euramet["B11"] = self.banco_di_taratura.euramet_unita_ingegneristica_di_misura
        sheet_euramet["B12"] = self.banco_di_taratura.euramet_Unità_ingegneristica_UUT
        sheet_euramet["B13"] = self.banco_di_taratura.controller_modbus.DATA.coefficiente_main
        sheet_euramet["B14"] = self.banco_di_taratura.euramet_Offset
        sheet_euramet["B20"] = self.banco_di_taratura.euramet_Coppia_taratura_MAX
        
        sheet_euramet["B63"] = self.banco_di_taratura.euramet_Data
        sheet_euramet["B64"] = self.banco_di_taratura.euramet_Rif_interno_attivita
        sheet_euramet["B65"] = self.banco_di_taratura.euramet_Cliente
        sheet_euramet["B66"] = self.banco_di_taratura.euramet_SN_TX
        sheet_euramet["B67"] = self.banco_di_taratura.euramet_Descrizione_UUT
        sheet_euramet["B68"] = self.banco_di_taratura.euramet_Progetto_UUT
        sheet_euramet["B69"] = self.banco_di_taratura.euramet_SN_UUT
        sheet_euramet["B70"] = self.banco_di_taratura.euramet_Report_di_calibrazione_TX
        
        self.banco_di_taratura.excell_path_certificate = f"python\\Codice_Progetto\\Certificati_Euramet_Completi\\{self.banco_di_taratura.excell_name}.xlsx"
        self.check_path()
        
    def update_steps(self):
        if self.banco_di_taratura.current_number_of_steps == 5:
            altezza_step = int(self.banco_di_taratura.euramet_Coppia_taratura_MAX)/5
            self.euramet_window.ui.label_step_1_5.setText(str(int(altezza_step*1)))
            self.euramet_window.ui.label_step_2_5.setText(str(int(altezza_step*2)))
            self.euramet_window.ui.label_step_3_5.setText(str(int(altezza_step*3)))
            self.euramet_window.ui.label_step_4_5.setText(str(int(altezza_step*4)))
            self.euramet_window.ui.label_step_5_5.setText(str(int(altezza_step*5)))
        elif self.banco_di_taratura.current_number_of_steps == 4:
            altezza_step = int(self.banco_di_taratura.euramet_Coppia_taratura_MAX)/4
            self.euramet_window.ui.label_step_1_4.setText(str(int(altezza_step*1)))
            self.euramet_window.ui.label_step_2_4.setText(str(int(altezza_step*2)))
            self.euramet_window.ui.label_step_3_4.setText(str(int(altezza_step*3)))
            self.euramet_window.ui.label_step_4_4.setText(str(int(altezza_step*4)))
        elif self.banco_di_taratura.current_number_of_steps == 3:
            altezza_step = int(self.banco_di_taratura.euramet_Coppia_taratura_MAX)/3
            self.euramet_window.ui.label_step_1_3.setText(str(int(altezza_step*1)))
            self.euramet_window.ui.label_step_2_3.setText(str(int(altezza_step*2)))
            self.euramet_window.ui.label_step_3_3.setText(str(int(altezza_step*3)))
        elif self.banco_di_taratura.current_number_of_steps == 2:
            altezza_step = int(self.banco_di_taratura.euramet_Coppia_taratura_MAX)/2
            self.euramet_window.ui.label_step_1_2.setText(str(int(altezza_step*1)))
            self.euramet_window.ui.label_step_2_2.setText(str(int(altezza_step*2)))
        elif self.banco_di_taratura.current_number_of_steps == 1:
            altezza_step = int(self.banco_di_taratura.euramet_Coppia_taratura_MAX)
            self.euramet_window.ui.label_step_1_1.setText(str(int(altezza_step)))

    def format_to_list(self, colonna, riga):
        formatted_list = [colonna, riga]
        return formatted_list
        
        # Controllare se il file esiste
    def check_path(self):
            if os.path.exists(self.banco_di_taratura.excell_path_certificate) and self.banco_di_taratura.excell_name != "Default":
                    print(f"Il file '{self.banco_di_taratura.excell_path_certificate}' esiste già. Non è stato sovrascritto.")
                    self.tmp = f"{self.banco_di_taratura.excell_name}_{self.counter_registrazione}"
                    self.banco_di_taratura.excell_path_certificate = f"python\\Codice_Progetto\\Certificati_Euramet_Completi\\{self.tmp}.xlsx"
                    self.counter_registrazione = self.counter_registrazione + 1
                    self.check_path()
                    # pop up con messaggio: inserire un nuovo nome al file di registrazione
            else:
                # Salvare il file excell
                self.workbook.save(self.banco_di_taratura.excell_path_certificate)
                if self.banco_di_taratura.excell_name == "Default": 
                        # print(f"Il file '{self.banco_di_taratura.excell_path_certificate}' è stato sovrascritto siccome era il file di default.")
                        error_window = Error_window(banco_di_taratura=self.banco_di_taratura)
                        error_window.set_error_message(f"Il file '{self.banco_di_taratura.excell_path_certificate}' \nè stato sovrascritto siccome era il file di default.")
                        error_window.setWindowTitle("Communication Window")
                        error_window.exec()
                elif self.counter_registrazione > 0:
                    # print(f"Il file '{self.banco_di_taratura.excell_path_certificate}' è stato salvato con successo.")
                        error_window = Error_window(banco_di_taratura=self.banco_di_taratura)
                        error_window.set_error_message(f"Il file '{self.banco_di_taratura.excell_path_certificate}' \nè stato salvato. Il nome è cambiato per evitare sovrascritture.")
                        error_window.setWindowTitle("Communication Window")
                        error_window.exec()
                else:
                        error_window = Error_window(banco_di_taratura=self.banco_di_taratura)
                        error_window.set_error_message(f"Il file '{self.banco_di_taratura.excell_path_certificate}' \nè stato salvato con successo.")
                        error_window.setWindowTitle("Communication Window")
                        error_window.exec()
                if self.tmp != None:
                    self.banco_di_taratura.excell_name = self.tmp