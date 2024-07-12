from __future__ import annotations
from PySide6.QtWidgets import QDialog
from Dialog_csv_euramet_ui import Ui_Dialog_csv_euramet
from typing import TYPE_CHECKING

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
        
    # segnali
        self.ui.pushButton_save_and_back.clicked.connect(self.save_and_back)
        
    def save_and_back(self):
        self.save_process()
        self.update_steps()
        self.euramet_window.show()
        self.close()
        
    def save_process(self):
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

        print(self.banco_di_taratura.euramet_unita_ingegneristica_di_misura,
              self.banco_di_taratura.euramet_Report_di_calibrazione_TX,
              self.banco_di_taratura.controller_modbus.DATA.coefficiente_main)
        
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

