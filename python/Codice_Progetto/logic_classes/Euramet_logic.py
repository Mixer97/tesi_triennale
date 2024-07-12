from __future__ import annotations
from PySide6.QtWidgets import QDialog
from typing import TYPE_CHECKING
from openpyxl import load_workbook

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from Mainwindow_grafico_logic import GraphWindow




class Rampa:
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, tipo, misura:Misura_euramet, misure_gia_fatte) -> None:
        
        """
        tipo --> "salita", "discesa", "zero finale"
        quadrante --> "Q1 (positivo)", "Q3 (negativo)"
        """
        
        self.tipo = tipo
        self.misure_gia_fatte = misure_gia_fatte
        self.misura_euramet = misura
        self.banco_di_taratura = banco_di_taratura
        self.number_of_steps = self.banco_di_taratura.current_number_of_steps+1  #numero step rampa (considero anche lo 0 quindi 1 step in più)
        self.status_altezza = self.banco_di_taratura.status_inserimento_altezza  #accetta altezza o no
        
        # Parametri
        self.step_attuale = 0
        self.excel_cell_quadrant_start = self.misura_euramet.starting_cell_address
        self.excel_path_template = self.banco_di_taratura.excell_path_template
        self.excel_path_certificate = self.banco_di_taratura.excell_path_certificate
        self.max_torque = misura.max_torque
        self.step_increment = int(int(self.max_torque)/int(self.number_of_steps))
        
        
    def measure_value(self):
        # Acquisizione dei 5 valori da mettere in tabella
        haxis = int(self.banco_di_taratura.axis_h)
        href = int(self.misura_euramet.graphwindow.ui.lineEdit_altezza.text())
        cella_di_carico_N = self.banco_di_taratura.controller_tcp.DATA.LIST_N_VALUE[1]
        torsiometro = self.banco_di_taratura.controller_tcp.DATA.LIST_Nm_VALUE[3]
        sg600 = self.banco_di_taratura.controller_modbus.DATA.canale_principale_Nm
        
        # Scrittura su Excell e aumento dello step
        data = (haxis, int(href), cella_di_carico_N, torsiometro, sg600)
        starting_row_cell = self.calculate_row_starting_cell()
        self.write_to_excell(data=data, starting_row_cell=starting_row_cell)
        self.increment_step()
        end_check = self.check_end()  # Se = 1 ha finito la rampa, se = 0 mancano delle misure
        return end_check
        
    
    def write_to_excell(self, data, starting_row_cell):
        tmp_cell = starting_row_cell    # inizia da questa cella e scrive i dati necessari
        for i in range(5):
            sheet_euramet = self.banco_di_taratura.workbook[self.banco_di_taratura.excell_page_data]
            tmp = self.misura_euramet.convert_cell_to_string(excell_column=tmp_cell[0],excell_row=tmp_cell[1])
            sheet_euramet[tmp] = data[i]
            tmp_cell[0] = self.misura_euramet.pointer_right_a_cell(tmp_cell)
        self.banco_di_taratura.workbook.save(self.excel_path_certificate)  
        
    def increment_step(self):
        self.step_attuale += 1
        # inserire cambiamento del valore nella label STEP sul graphwindow
        
    def check_stability(self):
        pass
    
    def check_end(self):
        # Torna 1 se la rampa è finita, 0 se ci sono ancora degli step
        if self.step_attuale == self.number_of_steps:
            return 1
        else:
            return 0
    
    def calculate_row_starting_cell(self):
        tmp = self.excel_cell_quadrant_start[1]
        tmp_cell = [self.excel_cell_quadrant_start[0], tmp]
        for i in range(self.step_attuale + self.misure_gia_fatte):
            tmp = self.misura_euramet.pointer_down_a_cell(tmp_cell)
            tmp_cell = [self.excel_cell_quadrant_start[0], tmp]
        row_starting_cell = [self.misura_euramet.starting_column, tmp]
        return row_starting_cell
        

class Precarichi:
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, misura:Misura_euramet):
        
        """
        quadrante --> "Q1 (positivo)", "Q3 (negativo)"
        """

        self.misura_euramet = misura
        self.banco_di_taratura = banco_di_taratura
        self.number_of_steps = 6  #numero step rampa
        self.status_altezza = self.banco_di_taratura.status_inserimento_altezza  #accetta altezza o no
        
        # Parametri
        self.step_attuale = 0
        self.excel_cell_quadrant_start = self.misura_euramet.starting_cell_address
        self.excel_path_template = self.banco_di_taratura.excell_path_template
        self.excel_path_certificate = self.banco_di_taratura.excell_path_certificate
        self.max_torque = misura.max_torque
        self.current_step_value = 0
        
    def measure_value(self):
        # Acquisizione dei 5 valori da mettere in tabella
        haxis = int(self.banco_di_taratura.axis_h)
        href = int(self.misura_euramet.graphwindow.ui.lineEdit_altezza.text())
        cella_di_carico_N = self.banco_di_taratura.controller_tcp.DATA.LIST_N_VALUE[1]  # cella ch2
        torsiometro = self.banco_di_taratura.controller_tcp.DATA.LIST_Nm_VALUE[3]  # cella ch4
        sg600 = self.banco_di_taratura.controller_modbus.DATA.canale_principale_Nm
        
        # Scrittura su Excell e aumento dello step
        data = (haxis, int(href), cella_di_carico_N, torsiometro, sg600)
        starting_row_cell = self.calculate_row_starting_cell()
        self.write_to_excell(data=data, starting_row_cell=starting_row_cell)
        self.increment_step()
        end_check = self.check_end()  # Se = 1 ha finito la rampa, se = 0 mancano delle misure
        return end_check
        
    
    def write_to_excell(self, data, starting_row_cell):
        tmp_cell = starting_row_cell    # inizia da questa cella e scrive i dati necessari
        tmp = 0
        for i in range(5):
            sheet_euramet = self.banco_di_taratura.workbook[self.banco_di_taratura.excell_page_data]
            tmp = self.misura_euramet.convert_cell_to_string(excell_column=tmp_cell[0],excell_row=tmp_cell[1])
            sheet_euramet[tmp] = data[i]
            tmp_cell[0] = self.misura_euramet.pointer_right_a_cell(tmp_cell)
        self.banco_di_taratura.workbook.save(self.excel_path_certificate)  
        
    def increment_step(self):
        self.step_attuale += 1
        self.prec_steps()
        # inserire cambiamento del valore nella label STEP sul graphwindow
        
        
    def check_stability(self):
        pass
    
    def prec_steps(self):
        if self.current_step_value == 0:
            self.current_step_value = self.max_torque
        elif self.current_step_value == self.max_torque:
            self.current_step_value = 0
    
    def check_end(self):
        # Torna 1 se la rampa è finita, 0 se ci sono ancora degli step
        if self.step_attuale == self.number_of_steps:
            return 1
        else:
            return 0
    
    def calculate_row_starting_cell(self):
        tmp = self.excel_cell_quadrant_start[1]
        tmp_cell = [self.excel_cell_quadrant_start[0], tmp]
        for i in range(self.step_attuale):
            tmp = self.misura_euramet.pointer_down_a_cell(tmp_cell)
            tmp_cell = [self.excel_cell_quadrant_start[0], tmp]
        row_starting_cell = [self.misura_euramet.starting_column, tmp]
        return row_starting_cell
    
class Misura_euramet:
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, graphwindow:GraphWindow):
        
        """
        quadrante --> "Q1 (positivo)", "Q3 (negativo)"
        canale 4 --> torsiometro, canale 2 --> cella di carico
        """
        self.graphwindow = graphwindow
        self.numero_misure_totali_da_fare = 0
        self.misure_fatte = 0
        self.banco_di_taratura = banco_di_taratura
        self.max_torque = self.check_quadrant_for_max_torque()
        self.starting_cell_address = self.check_excell_cell_by_quadrant()
        self.end_check_prec = 0
        self.end_check_salita_1 = 0
        self.end_check_discesa_1 = 0
        self.end_check_salita_2 = 0
        self.end_check_zero_finale = 0
        self.starting_column = self.banco_di_taratura.euramet_cella_inizio_precarichi_Q1[0]
        
        # dati che controllano il proseguimento di euramet
        self.quandrant_counter = 0
        
        # Creazione delle entità che compongono Euramet in un certo Quadrante
        self.precarichi = Precarichi(self.banco_di_taratura, self)
        self.numero_misure_totali_da_fare += 6
        if self.banco_di_taratura.list_status_checkbox_euramet_page[0] == 1:
            self.rampa_salita_1 = Rampa(self.banco_di_taratura, misura=self, tipo="salita", misure_gia_fatte=self.numero_misure_totali_da_fare)
            self.numero_misure_totali_da_fare += self.rampa_salita_1.number_of_steps
        else:
            self.rampa_salita_1 = None
        if self.banco_di_taratura.list_status_checkbox_euramet_page[1] == 1:
            self.rampa_discesa_1 = Rampa(self.banco_di_taratura, misura=self, tipo="discesa", misure_gia_fatte=self.numero_misure_totali_da_fare)
            self.numero_misure_totali_da_fare += self.rampa_discesa_1.number_of_steps
        else:
            self.rampa_discesa_1 = None
        if self.banco_di_taratura.list_status_checkbox_euramet_page[2] == 1:
            self.rampa_salita_2 = Rampa(self.banco_di_taratura, misura=self, tipo="salita", misure_gia_fatte=self.numero_misure_totali_da_fare)
            self.numero_misure_totali_da_fare += self.rampa_salita_2.number_of_steps
            self.zero_finale = Rampa(self.banco_di_taratura, misura=self, tipo ="zero finale", misure_gia_fatte=self.numero_misure_totali_da_fare)
            self.numero_misure_totali_da_fare += 1
        else:
            self.rampa_salita_2 = None
            self.zero_finale = None
        # Ora ho il numero totale di misure da fare

    def measure_value(self):
        if self.end_check_prec == 0:
            print("sono nei precarichi")
            self.end_check_prec = self.precarichi.measure_value()
        elif self.end_check_salita_1 == 0 and self.rampa_salita_1 != None:
            print("sono nella salita 1")
            self.end_check_salita_1 = self.rampa_salita_1.measure_value()
        elif self.end_check_discesa_1 == 0 and self.rampa_discesa_1 != None:
            print("sono nella discesa 1")
            self.end_check_discesa_1 = self.rampa_discesa_1.measure_value()
        elif self.end_check_salita_2 == 0 and self.rampa_salita_2 != None:
            print("sono nella salita 2")
            self.end_check_salita_2 = self.rampa_salita_2.measure_value()
        elif self.end_check_zero_finale == 0 and self.zero_finale != None:
            self.end_check_zero_finale = self.zero_finale.measure_value()
            if self.end_check_zero_finale == 1:
                self.number_of_steps = 1
                self.max_torque = 0
                self.banco_di_taratura.quadrant_counter += 1
            
            print("Sono nello zero finale")
        else:
            print("qui non ci deve arrivare!")

        
    def check_quadrant_for_max_torque(self):
        if self.banco_di_taratura.quadrant == "Q3":
            torque_max = -(self.banco_di_taratura.euramet_Coppia_taratura_MAX)
        else:
            torque_max = self.banco_di_taratura.euramet_Coppia_taratura_MAX
        return torque_max

    def check_excell_cell_by_quadrant(self):
        if self.banco_di_taratura.quadrant == "Q3":
            starting_cell_address = self.banco_di_taratura.euramet_cella_inizio_precarichi_Q3
        else: 
            starting_cell_address = self.banco_di_taratura.euramet_cella_inizio_precarichi_Q1
        return starting_cell_address
    
    def pointer_right_a_cell(self, cell):
        # Carattere corrente
        char = cell[0]
        # Converti il carattere in valore ASCII, incrementa di 1 e poi riconverti in carattere
        next_char = chr(ord(char) + 1) 
        return(next_char)
        
    def pointer_left_a_cell(self, cell):
        # Carattere corrente
        char = cell[0]
        # Converti il carattere in valore ASCII, incrementa di 1 e poi riconverti in carattere
        next_char = chr(ord(char) - 1)
        return(next_char)
    
    def pointer_down_a_cell(self, cell):
        # Colonna corrente
        int = cell[1]
        # Cambia il valore della colonna
        int += 1
        return(int)
    
    def pointer_up_a_cell(self, cell):
        # Colonna corrente
        int = cell[1]
        # Cambia il valore della colonna
        int -= 1
        print(int)
        return(int)
    
    def convert_cell_to_string(self, excell_column, excell_row):
        str_cell = f"{excell_column}{excell_row}"
        return(str_cell)