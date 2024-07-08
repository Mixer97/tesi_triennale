from __future__ import annotations
from typing import TYPE_CHECKING
import json


if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from View_QT_SetupPage_logic import SetupWindow
    
    
def load_setup(nome_file, banco_di_taratura:BANCO_DI_TARATURA, setup_window:SetupWindow):
    setup_window.ui.label_banco_attuale.setText(str(nome_file))
    with open(nome_file, "r", encoding="utf-8") as json_string:
        new_json_string = json.load(json_string)
        
        # Banco
        banco_di_taratura.list_status_checkbox = new_json_string['data_banco']['status checkbox']
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
        
        print(new_json_string)

def save_setup(nome_file, banco_di_taratura:BANCO_DI_TARATURA):
        
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
    data_banco["status checkbox"] = banco_di_taratura.list_status_checkbox
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
    
    with open(f"python\\Codice_Progetto\\JSON\\{nome_file}.json", "w", encoding="utf-8") as write_file:
        json.dump(data, write_file, indent=4)
        json_string = json.dumps(data, indent=4)
        print(json_string)