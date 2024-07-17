from __future__ import annotations
from typing import TYPE_CHECKING
import json
import Dialog_salavataggio_setup_logic
import os
from Dialog_error_logic import Error_window

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from View_QT_SetupPage_logic import SetupWindow
    from Dialog_xlxs_euramet_logic import csv_euramet_window
    
class handler_json:  
            
    def __init__(self, nome_file_load="", nome_file_save=""):
        self.counter_salvataggio = 0
        self.nome_file_load = nome_file_load
        self.nome_file_save = nome_file_save
        
        # banco
        self.path_load_banco=f"python\\Codice_Progetto\\JSON\\Setup_banco\\{os.path.basename(self.nome_file_load)}"
        self.path_save_banco=f"python\\Codice_Progetto\\JSON\\Setup_banco\\{self.nome_file_save}.json"
        self.tmp_banco = None
        
        # euramet
        self.path_load_euramet=f"python\\Codice_Progetto\\JSON\\Setup_Euramet\\{os.path.basename(self.nome_file_load)}"
        self.path_save_euramet=f"python\\Codice_Progetto\\JSON\\Setup_Euramet\\{self.nome_file_save}.json"
        self.tmp_euramet = None
        
    
    def load_setup_banco(self, banco_di_taratura:BANCO_DI_TARATURA, setup_window:SetupWindow):
        setup_window.ui.label_banco_attuale.setText(str(self.nome_file_load))
        with open(self.nome_file_load, "r", encoding="utf-8") as json_string:
            new_json_string = json.load(json_string)
            
            # Banco
            banco_di_taratura.list_status_checkbox_setup_page = new_json_string['data_banco']['status checkbox']
            banco_di_taratura.file_setup_banco_name = new_json_string['data_banco']['file setup name']
            # C_modbus
            banco_di_taratura.controller_modbus.DATA.zero_main = new_json_string['data_controller_modbus']['zero main']
            banco_di_taratura.controller_modbus.DATA.coefficiente_main = new_json_string['data_controller_modbus']['coefficiente main']
            banco_di_taratura.controller_modbus.DATA.zero_temp = new_json_string['data_controller_modbus']['zero temp']
            banco_di_taratura.controller_modbus.DATA.coefficiente_temp = new_json_string['data_controller_modbus']['coefficiente temp']
            # C_tcp
            banco_di_taratura.controller_tcp.DATA.LIST_SENSIBILITY = new_json_string['data_controller_tcp']['list sensibility']
            banco_di_taratura.controller_tcp.DATA.LIST_FULLSCALE = new_json_string['data_controller_tcp']['list fullscale']
            banco_di_taratura.controller_tcp.DATA.LIST_mV_ZERO = new_json_string['data_controller_tcp']['list mV zero']
            banco_di_taratura.controller_tcp.DATA.LEVER_LENGTH = new_json_string['data_controller_tcp']['lever length']
            banco_di_taratura.controller_tcp.DATA.STATUS_CHANNELS = new_json_string['data_controller_tcp']['status channels']
            # Logger
            banco_di_taratura.logger.DATA.periodo_logger = new_json_string['data_logger']['periodo logger']
            
            # print(new_json_string)
            error_window = Error_window(banco_di_taratura=banco_di_taratura)
            error_window.set_error_message(f"Il file '{self.path_load_banco}' \nè stato caricato con successo.")
            error_window.setWindowTitle("Communication Window")
            error_window.exec()

    def save_setup_banco(self, banco_di_taratura:BANCO_DI_TARATURA, dialog_window:Dialog_salavataggio_setup_logic):
        
        if os.path.exists(self.path_save_banco) and self.nome_file_save != "Default":   # cicla finche non trova un nome disponibile
            print(f"Il file '{self.path_save_banco}' esiste già. Non è stato sovrascritto.")
            self.tmp_banco = f"{self.nome_file_save}_{self.counter_salvataggio}"
            self.path_save_banco = 'python\\Codice_Progetto\\JSON\\Setup_banco\\' + str(self.tmp_banco) + ".json"
            self.counter_salvataggio = self.counter_salvataggio + 1
            self.save_setup_banco(banco_di_taratura, dialog_window)
            
        else:
            # dati da salvare
            data_banco={}
            data_controller_modbus={}
            data_controller_tcp={}
            data_logger={}
            
            data = {
                'data_banco': data_banco,
                'data_controller_modbus': data_controller_modbus,
                'data_controller_tcp': data_controller_tcp,
                'data_logger': data_logger
            }
            
            # Banco
            data_banco["status checkbox"] = banco_di_taratura.list_status_checkbox_setup_page
            data_banco["file setup name"] = banco_di_taratura.file_setup_banco_name
            # C_modbus
            data_controller_modbus["zero main"] = banco_di_taratura.controller_modbus.DATA.zero_main
            data_controller_modbus["coefficiente main"] = banco_di_taratura.controller_modbus.DATA.coefficiente_main
            data_controller_modbus["zero temp"] = banco_di_taratura.controller_modbus.DATA.zero_temp
            data_controller_modbus["coefficiente temp"] = banco_di_taratura.controller_modbus.DATA.coefficiente_temp
            # C_tcp
            data_controller_tcp["list sensibility"] = banco_di_taratura.controller_tcp.DATA.LIST_SENSIBILITY
            data_controller_tcp["list fullscale"] = banco_di_taratura.controller_tcp.DATA.LIST_FULLSCALE
            data_controller_tcp["list mV zero"] = banco_di_taratura.controller_tcp.DATA.LIST_mV_ZERO
            data_controller_tcp["lever length"] = banco_di_taratura.controller_tcp.DATA.LEVER_LENGTH
            data_controller_tcp["status channels"] = banco_di_taratura.controller_tcp.DATA.STATUS_CHANNELS
            # Logger
            data_logger["periodo logger"] = banco_di_taratura.logger.DATA.periodo_logger
            
            with open(self.path_save_banco, "w", encoding="utf-8") as write_file:
                json.dump(data, write_file, indent=4)
                json_string = json.dumps(data, indent=4)
                print(json_string)        
                
            if self.nome_file_save == "Default": 
                # print(f"Il file '{self.path_save_banco}' è stato sovrascritto siccome era il file di default.")
                error_window = Error_window(banco_di_taratura=banco_di_taratura)
                error_window.set_error_message(f"Il file '{self.path_save_banco}' \nè stato sovrascritto siccome era il file di default.")
                error_window.setWindowTitle("Communication Window")
                error_window.exec()
            elif self.counter_salvataggio > 0:
                # print(f"Il file '{self.path_save_banco}' è stato salvato con successo.")
                error_window = Error_window(banco_di_taratura=banco_di_taratura)
                error_window.set_error_message(f"Il file '{self.path_save_banco}' \nè stato salvato. Il nome è cambiato per evitare sovrascritture.")
                error_window.setWindowTitle("Communication Window")
                error_window.exec()
            else:
                error_window = Error_window(banco_di_taratura=banco_di_taratura)
                error_window.set_error_message(f"Il file '{self.path_save_banco}' \nè stato salvato con successo.")
                error_window.setWindowTitle("Communication Window")
                error_window.exec()
            if self.tmp_banco != None:
                self.nome_file_save = self.tmp_banco
                
                
    def load_setup_euramet(self, banco_di_taratura:BANCO_DI_TARATURA, setup_window_euramet:csv_euramet_window):
        setup_window_euramet.ui.label_euramet_attuale.setText(str(self.nome_file_load))
        with open(self.nome_file_load, "r", encoding="utf-8") as json_string:
            new_json_string = json.load(json_string)
            
            banco_di_taratura.euramet_unita_ingegneristica_di_misura = new_json_string['euramet_unita_ingegneristica_di_misura']
            banco_di_taratura.euramet_Unità_ingegneristica_UUT = new_json_string['euramet_Unità_ingegneristica_UUT']
            banco_di_taratura.controller_modbus.DATA.coefficiente_main = new_json_string['euramet_Scale']
            banco_di_taratura.euramet_Offset = new_json_string['euramet_Offset']
            banco_di_taratura.euramet_Coppia_taratura_MAX = new_json_string['euramet_Coppia_taratura_MAX']
            banco_di_taratura.euramet_Data = new_json_string['euramet_Data']
            banco_di_taratura.euramet_Rif_interno_attivita = new_json_string['euramet_Rif_interno_attivita']
            banco_di_taratura.euramet_Cliente = new_json_string['euramet_Cliente']
            banco_di_taratura.euramet_SN_TX = new_json_string['euramet_SN_TX']
            banco_di_taratura.euramet_Descrizione_UUT = new_json_string['euramet_Descrizione_UUT']
            banco_di_taratura.euramet_Progetto_UUT = new_json_string['euramet_Progetto_UUT']
            banco_di_taratura.euramet_SN_UUT = new_json_string['euramet_SN_UUT']
            banco_di_taratura.euramet_Report_di_calibrazione_TX = new_json_string['euramet_Report_di_calibrazione_TX']
            
            banco_di_taratura.list_status_checkbox_euramet_page = new_json_string['list_status_checkbox_euramet_page']
            banco_di_taratura.status_inserimento_altezza = new_json_string['status_inserimento_altezza']
            banco_di_taratura.euramet_cella_inizio_precarichi_Q3 = new_json_string['euramet_cella_inizio_precarichi_Q3']
            banco_di_taratura.euramet_cella_inizio_precarichi_Q1 = new_json_string['euramet_cella_inizio_precarichi_Q1']
            
            banco_di_taratura.excell_name = new_json_string['excell_name']
            banco_di_taratura.excell_page_data = new_json_string['excell_page_data']
            
            # print(new_json_string)
            error_window = Error_window(banco_di_taratura=banco_di_taratura)
            error_window.set_error_message(f"Il file '{self.path_load_banco}' \nè stato caricato con successo.")
            error_window.setWindowTitle("Communication Window")
            error_window.exec()

    def save_setup_euramet(self, banco_di_taratura:BANCO_DI_TARATURA, setup_window_euramet:csv_euramet_window):
        
        if os.path.exists(self.path_save_euramet) and self.nome_file_save != "Default":   # cicla finche non trova un nome disponibile
            print(f"Il file '{self.path_save_euramet}' esiste già. Non è stato sovrascritto.")
            self.tmp_banco = f"{self.nome_file_save}_{self.counter_salvataggio}"
            self.path_save_euramet = 'python\\Codice_Progetto\\JSON\\Setup_Euramet\\' + str(self.tmp_banco) + ".json"
            self.counter_salvataggio = self.counter_salvataggio + 1
            self.save_setup_euramet(banco_di_taratura, setup_window_euramet)
            
        else:
            
            data = {}
            
            data["euramet_unita_ingegneristica_di_misura"] = banco_di_taratura.euramet_unita_ingegneristica_di_misura
            data["euramet_Unità_ingegneristica_UUT"] = banco_di_taratura.euramet_Unità_ingegneristica_UUT
            data["euramet_Scale"] = banco_di_taratura.controller_modbus.DATA.coefficiente_main
            data["euramet_Offset"] = banco_di_taratura.euramet_Offset
            data["euramet_Coppia_taratura_MAX"] = banco_di_taratura.euramet_Coppia_taratura_MAX
            data["euramet_Data"] = banco_di_taratura.euramet_Data
            data["euramet_Rif_interno_attivita"] = banco_di_taratura.euramet_Rif_interno_attivita
            data["euramet_Cliente"] = banco_di_taratura.euramet_Cliente
            data["euramet_SN_TX"] = banco_di_taratura.euramet_SN_TX
            data["euramet_Descrizione_UUT"] = banco_di_taratura.euramet_Descrizione_UUT
            data["euramet_Progetto_UUT"] = banco_di_taratura.euramet_Progetto_UUT
            data["euramet_SN_UUT"] = banco_di_taratura.euramet_SN_UUT
            data["euramet_Report_di_calibrazione_TX"] = banco_di_taratura.euramet_Report_di_calibrazione_TX
            
            data["list_status_checkbox_euramet_page"] = banco_di_taratura.list_status_checkbox_euramet_page
            data["status_inserimento_altezza"] = banco_di_taratura.status_inserimento_altezza
            data["euramet_cella_inizio_precarichi_Q3"] = banco_di_taratura.euramet_cella_inizio_precarichi_Q3
            data["euramet_cella_inizio_precarichi_Q1"] = banco_di_taratura.euramet_cella_inizio_precarichi_Q1
            
            data["excell_name"] = banco_di_taratura.excell_name
            data["excell_page_data"] = banco_di_taratura.excell_page_data

            
            with open(self.path_save_euramet, "w", encoding="utf-8") as write_file:
                json.dump(data, write_file, indent=4)
                json_string = json.dumps(data, indent=4)
                print(json_string)        
                
            if self.nome_file_save == "Default": 
                # print(f"Il file '{self.path_save_euramet}' è stato sovrascritto siccome era il file di default.")
                error_window = Error_window(banco_di_taratura=banco_di_taratura)
                error_window.set_error_message(f"Il file '{self.path_save_euramet}' \nè stato sovrascritto siccome era il file di default.")
                error_window.setWindowTitle("Communication Window")
                error_window.exec()
            elif self.counter_salvataggio > 0:
                # print(f"Il file '{self.path_save_euramet}' è stato salvato con successo.")
                error_window = Error_window(banco_di_taratura=banco_di_taratura)
                error_window.set_error_message(f"Il file '{self.path_save_euramet}' \nè stato salvato. Il nome è cambiato per evitare sovrascritture.")
                error_window.setWindowTitle("Communication Window")
                error_window.exec()
            else:
                error_window = Error_window(banco_di_taratura=banco_di_taratura)
                error_window.set_error_message(f"Il file '{self.path_save_euramet}' \nè stato salvato con successo.")
                error_window.setWindowTitle("Communication Window")
                error_window.exec()
            if self.tmp_banco != None:
                self.nome_file_save = self.tmp_banco
        

            

            
        