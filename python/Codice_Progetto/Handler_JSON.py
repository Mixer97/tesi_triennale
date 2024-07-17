from __future__ import annotations
from typing import TYPE_CHECKING
import json
import Dialog_salavataggio_setup_logic
import os
from Dialog_error_logic import Error_window

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from View_QT_SetupPage_logic import SetupWindow
    
class handler_json:  
            
    def __init__(self, nome_file_load="", nome_file_save=""):
        self.counter_salvataggio = 0
        self.nome_file_load = nome_file_load
        self.nome_file_save = nome_file_save
        self.path_load=f"python\\Codice_Progetto\\JSON\\{os.path.basename(self.nome_file_load)}"
        self.path_save=f"python\\Codice_Progetto\\JSON\\{self.nome_file_save}.json"
        self.tmp = None
    
    def load_setup(self, banco_di_taratura:BANCO_DI_TARATURA, setup_window:SetupWindow):
        setup_window.ui.label_banco_attuale.setText(str(self.nome_file_load))
        with open(self.nome_file_load, "r", encoding="utf-8") as json_string:
            new_json_string = json.load(json_string)
            
            # Banco
            banco_di_taratura.list_status_checkbox_setup_page = new_json_string['data_banco']['status checkbox']
            banco_di_taratura.file_setup_name = new_json_string['data_banco']['file setup name']
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
            error_window.set_error_message(f"Il file '{self.path_load}' \nè stato caricato con successo.")
            error_window.setWindowTitle("Communication Window")
            error_window.exec()

    def save_setup(self, banco_di_taratura:BANCO_DI_TARATURA, dialog_window:Dialog_salavataggio_setup_logic):
        
        if os.path.exists(self.path_save) and self.nome_file_save != "Default":   # cicla finche non trova un nome disponibile
            print(f"Il file '{self.path_save}' esiste già. Non è stato sovrascritto.")
            self.tmp = f"{self.nome_file_save}_{self.counter_salvataggio}"
            self.path_save = 'python\\Codice_Progetto\\JSON\\' + str(self.tmp) + ".json"
            self.counter_salvataggio = self.counter_salvataggio + 1
            self.save_setup(banco_di_taratura, dialog_window)
            
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
            data_banco["file setup name"] = banco_di_taratura.file_setup_name
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
            
            with open(self.path_save, "w", encoding="utf-8") as write_file:
                json.dump(data, write_file, indent=4)
                json_string = json.dumps(data, indent=4)
                print(json_string)        
                
            if self.nome_file_save == "Default": 
                # print(f"Il file '{self.path_save}' è stato sovrascritto siccome era il file di default.")
                error_window = Error_window(banco_di_taratura=banco_di_taratura)
                error_window.set_error_message(f"Il file '{self.path_save}' \nè stato sovrascritto siccome era il file di default.")
                error_window.setWindowTitle("Communication Window")
                error_window.exec()
            elif self.counter_salvataggio > 0:
                # print(f"Il file '{self.path_save}' è stato salvato con successo.")
                error_window = Error_window(banco_di_taratura=banco_di_taratura)
                error_window.set_error_message(f"Il file '{self.path_save}' \nè stato salvato. Il nome è cambiato per evitare sovrascritture.")
                error_window.setWindowTitle("Communication Window")
                error_window.exec()
            else:
                error_window = Error_window(banco_di_taratura=banco_di_taratura)
                error_window.set_error_message(f"Il file '{self.path_save}' \nè stato salvato con successo.")
                error_window.setWindowTitle("Communication Window")
                error_window.exec()
            if self.tmp != None:
                self.nome_file_save = self.tmp
        

            

            
        