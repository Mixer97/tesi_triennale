from __future__ import annotations
from PySide6.QtWidgets import QDialog
from typing import TYPE_CHECKING
from openpyxl import load_workbook
from Mainwindow_grafico_logic import GraphWindow

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA




class Rampa:
    def __init__(self, tipo, banco_di_taratura:BANCO_DI_TARATURA, misura:Misura_euramet) -> None:
        
        """
        tipo --> "salita", "discesa"
        quadrante --> "Q1 (positivo)", "Q3 (negativo)"
        """
        
        self.tipo = tipo
        self.misura_euramet = misura
        self.banco_di_taratura = banco_di_taratura
        self.number_of_steps = self.banco_di_taratura.current_number_of_steps  #numero step rampa
        self.status_altezza = self.banco_di_taratura.status_inserimento_altezza  #accetta altezza o no
        
        # Parametri
        self.step_attuale = 0
        self.excel_cell_to_write = self.misura_euramet.starting_cell_address
        self.excel_path_template = self.banco_di_taratura.excel_path_template
        self.excel_path_certificate = self.banco_di_taratura.excel_path_certificate
        self.max_torque = misura.max_torque
        self.step_increment = int(self.max_torque/self.number_of_steps)
        
        # Azioni
        if self.tipo == "salita":
            misura.graphwindow.ui.label_step_attuale_valore.setText("0 Nm")
        else:
            misura.graphwindow.ui.label_step_attuale_valore.setText(f"{self.max_torque}") 
        
        
        
    def measure_value(self):
        href = self.misura_euramet.graphwindow.ui.lineEdit_altezza.text()
        cella_di_carico_N = self.banco_di_taratura.controller_tcp.DATA.LIST_N_VALUE[1]
        torsiometro = self.banco_di_taratura.controller_tcp.DATA.LIST_Nm_VALUE[3]
        sg600 = self.banco_di_taratura.controller_modbus.DATA.canale_principale_Nm
        data = (href, cella_di_carico_N, torsiometro, sg600)
        self.write_to_excel(data=data)
        self.increment_step()
        
    
    def write_to_excel(self, data):
        # gestisco qui la scrittura nell excell e sposto il puntatore alla cella 
        data = (0,0,0,0)
        pass    
        
    def increment_step(self):
        self.step_attuale += 1
        
    def check_stability(self):
        pass
    

class Precarichi:
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, misura:Misura_euramet):
        
        """
        quadrante --> "Q1 (positivo)", "Q3 (negativo)"
        """
        
        self.banco_di_taratura = banco_di_taratura
        
        # Parametri
        self.step_attuale = 0   
        self.status_altezza = self.banco_di_taratura.status_inserimento_altezza  #accetta altezza o no
        self.excel_cell_to_write = None
        self.excel_path_template = self.banco_di_taratura.excel_path_template
        self.excel_path_certificate = self.banco_di_taratura.excel_path_certificate
        self.max_torque = misura.max_torque

        
    def measure_value(self):
        pass
        
    def write_ti_excel(self):
        pass    
        
    def increment_step(self):
        self.step_attuale += 1
        
    def check_stability(self):
        pass
    
    
class Misura_euramet:
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, graphwindow:GraphWindow):
        
        """
        quadrante --> "Q1 (positivo)", "Q3 (negativo)"
        """
        
        self.graphwindow = graphwindow
        self.numero_misure_totali_da_fare = 0
        self.misure_fatte = 0
        self.banco_di_taratura = banco_di_taratura
        self.max_torque = self.check_quadrant_for_max_torque()
        self.starting_cell_address = self.check_excell_cell()
        
        # Creazione delle entità che compongono Euramet in un certo Quadrante
        Precarichi(self.banco_di_taratura, self)
        self.numero_misure_totali_da_fare += 6
        if self.banco_di_taratura.list_status_checkbox_euramet_page[0] == 1:
            rampa_salita_1 = Rampa(self.banco_di_taratura, self, tipo="salita")
            self.numero_misure_totali_da_fare += rampa_salita_1.number_of_steps
        else:
            rampa_salita_1 = None
        if self.banco_di_taratura.list_status_checkbox_euramet_page[1] == 1:
            rampa_discesa_1 = Rampa(self.banco_di_taratura, self, tipo="discesa")
            self.numero_misure_totali_da_fare += rampa_discesa_1.number_of_steps
        else:
            rampa_discesa_1 = None
        if self.banco_di_taratura.list_status_checkbox_euramet_page[2] == 1:
            rampa_salita_2 = Rampa(self.banco_di_taratura, self, tipo="salita")
            self.numero_misure_totali_da_fare += rampa_salita_2.number_of_steps
        else:
            rampa_salita_2 = None
        # Ora ho il numero totale di misure da fare

        
    def check_quadrant_for_max_torque(self):
        if self.banco_di_taratura.quadrant == "Q3":
            torque_max = -(self.banco_di_taratura.euramet_Coppia_taratura_MAX)
        else:
            torque_max = self.banco_di_taratura.euramet_Coppia_taratura_MAX
        return torque_max

    def check_excell_cell(self):
        if self.banco_di_taratura.quadrant == "Q3":
            starting_cell_address = self.banco_di_taratura.euramet_cella_inizio_precarichi_Q3
        else: 
            starting_cell_address = self.banco_di_taratura.euramet_cella_inizio_precarichi_Q1
        return starting_cell_address