from __future__ import annotations
from typing import TYPE_CHECKING
from pymodbus.client import ModbusSerialClient
from pymodbus.framer import Framer
from pymodbus import pymodbus_apply_logging_config
from time import sleep
from logic_classes.Dialog_error_logic import Error_window
import logging 

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA

# print(sys.prefix)
class Controller_MODBUS:  
        
    class SLAVE:        # Comunicazione su RS-232
        def __init__(self, port, baudrate, bytesize, parity, stopbits, ID):
            self.port=port
            self.baudrate=baudrate
            self.bytesize=bytesize
            self.parity=parity
            self.stopbits=stopbits
            self.ID=ID
        
    class DATA:
        def __init__(self):
            
            # main
            self.canale_principale_mV=0 # Input canale 1
            self.canale_principale_Nm=0
            self.zero_main=0
            self.coefficiente_main = 1  # Nm/mV
            
            # temp
            self.canale_temperatura_mV=0  # Input canale 2
            self.canale_temperatura_C=0
            self.zero_temp=0
            self.coefficiente_temp = 1  # C/mV
            
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, port="COM8", baudrate=2400, bytesize=8, parity="N", stopbits=1, ID=1):
        self.SLAVE = self.SLAVE(port, baudrate, bytesize, parity, stopbits, ID)
        self.DATA = self.DATA()
        self.banco_di_taratura = banco_di_taratura
        self.client = ModbusSerialClient(
            method='rtu',
            port=self.SLAVE.port,
            baudrate=self.SLAVE.baudrate,
            bytesize=self.SLAVE.bytesize,
            parity=self.SLAVE.parity,
            stopbits=self.SLAVE.stopbits
        )

    """---------------------------CONNECT-----------------------------"""

    # Connessione al dispositivo Seneca
    def connect(self):
        try:
            connection = self.client.connect() 
            for i in range(1,4):
                if connection:
                    return True
                else: 
                    sleep(2)
                    logging.error(f"ERROR! connessione al dispostivo presente sulla COM-port {self.SLAVE.port} fallita.\n tentativo di riconnessione numero: {i}\\3", exc_info=True)
                    self.banco_di_taratura.error_window_logic(messaggio_di_errore=f"ERROR! connessione fallita con scheda Seneca, tentativo di riconnessione: {i}\\3.\nChiudere la finestra per continuare.")
                    connection = self.client.connect() 
        except Exception as e:
            logging.error("Connessione fallita dopo 3 tentativi!", exc_info=True)
            self.banco_di_taratura.error_window_logic(messaggio_di_errore=f"ERROR! connessione fallita con scheda Seneca, chiudere la finestra\ne riavviare l'applicazione.")
            return False

    """---------------------------WORKING-----------------------------"""      
        
    def read_MachineID(self):
        try:
            risultati = self.client.read_holding_registers(address=0, count=1, slave=self.SLAVE.ID)
            while risultati.isError():
                risultati = self.client.read_holding_registers(address=0, count=1, slave=self.SLAVE.ID)
            risultati_elaborati = risultati
            return risultati_elaborati
        except Exception as e:
            logging.exception("Exception occurred", exc_info=True)
    
    def read_holding_registers_mV(self):
        try:
            list_results_mV = [0,0]
            while list_results_mV == [0,0]:
                list_results_mV = self.read_registers(start_address=16, count=2)
            return list_results_mV
        except Exception as e:
            logging.exception("Exception occurred", exc_info=True)
            
    """---------------------------UTILS-----------------------------"""
     
    def read_registers(self, start_address, count):
        if self.connect():
            try:
                response = self.client.read_holding_registers(address=start_address, count=count, slave=self.SLAVE.ID)
                if not response.isError():
                    return response.registers
                else: 
                    logging.exception("Errore nella lettura dei registri.", exc_info=True)
            except Exception as e:
                logging.exception("Exception occurred", exc_info=True)
        else:
            logging.exception("Connessione non riuscita.", exc_info=True)
        return None
    
    """---------------------------DATA INTERACTIONS-----------------------------"""
    
    def get_mV_main(self):
        try:
            y = self.DATA.canale_principale_mV*self.banco_di_taratura.m_main + self.banco_di_taratura.q_main
            return y
        except Exception as e:
                logging.exception("Exception occurred", exc_info=True)
    
    def get_Nm_main(self):
        try:
            self.DATA.canale_principale_Nm = (self.get_mV_main() - self.DATA.zero_main) * self.DATA.coefficiente_main
            return self.DATA.canale_principale_Nm
        except Exception as e:
                logging.exception("Exception occurred", exc_info=True)
    
    def get_mV_temp(self):
        try:
            y = self.DATA.canale_temperatura_mV*self.banco_di_taratura.m_temp + self.banco_di_taratura.q_temp
            return y
        except Exception as e:
                logging.exception("Exception occurred", exc_info=True)
    
    def get_C_temp(self):
        try:
            self.DATA.canale_temperatura_C = (self.get_mV_temp() - self.DATA.zero_temp) * self.DATA.coefficiente_temp
            return self.DATA.canale_temperatura_C
        except Exception as e:
                logging.exception("Exception occurred", exc_info=True)
            
if __name__ == "__main__":
    controller=Controller_MODBUS()
    controller.DATA.canale_principale_mV = controller.read_registers(start_address=16, count=1)
    test=controller.read_registers(start_address=24, count=6)
    print(f"Registri letti: {controller.DATA.canale_principale_mV}")
    print(f"Registri letti normalizzati: {test}")
    
        