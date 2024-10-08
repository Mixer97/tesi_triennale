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

class Controller_MODBUS:  
        
    # oggetti slave contengono le informazioni principali per la connessione con il dispositivo #
    class SLAVE:        # Comunicazione su RS-232
        def __init__(self, port, baudrate, bytesize, parity, stopbits, ID):
            self.port=port
            self.baudrate=baudrate
            self.bytesize=bytesize
            self.parity=parity
            self.stopbits=stopbits
            self.ID=ID
        
    # dati attuali misurati #    
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
            
    # costruttore della classe #
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
    # Metodo usato per connettersi al dispositivo e che riprova fino a 2 volte in caso di perdita di connessione #
    def connect(self):
        try:
            connection = self.client.connect() 
            for i in range(1,3):
                if connection:
                    return True
                else: 
                    logging.warning(f"ERROR! connessione al dispostivo presente sulla COM-port {self.SLAVE.port} fallita.\n tentativo di riconnessione numero: {i}\\2", exc_info=True)
                    self.banco_di_taratura.error_window_logic(messaggio_di_errore=f"ERROR! connessione fallita con scheda Seneca, tentativo di riconnessione: {i}\\2.\nChiudere la finestra per continuare.")
                    # connection = self.client.connect() 
        except Exception as e:
            logging.warning("Connessione fallita dopo 3 tentativi!", exc_info=True)
            self.banco_di_taratura.error_window_logic(messaggio_di_errore=f"ERROR! connessione fallita con scheda Seneca, chiudere la finestra\ne riavviare l'applicazione.")
            return False

    """---------------------------WORKING-----------------------------"""      
    
    # Metodo che ritorna l'ID del dispositivo #
    def read_MachineID(self):
        try:
            risultati = self.client.read_holding_registers(address=0, count=1, slave=self.SLAVE.ID)
            while risultati.isError():
                risultati = self.client.read_holding_registers(address=0, count=1, slave=self.SLAVE.ID)
            risultati_elaborati = risultati
            return risultati_elaborati
        except Exception as e:
            logging.warning("Exception occurred", exc_info=True)
    
    # Metodo che legge i registri 4017 e 4018 della scheda Seneca #
    def read_holding_registers_mV(self):
        try:
            list_results_mV = [0,0]
            while list_results_mV == None:
                list_results_mV = self.read_registers(start_address=16, count=2)
            return list_results_mV
        except Exception as e:
            logging.warning("Exception occurred", exc_info=True)
            self.banco_di_taratura.error_window_logic(messaggio_di_errore="Errore nella lettura dei registri\n assicurarsi la connessione con la scheda Seneca!")
            
    """---------------------------UTILS-----------------------------"""
     
    # Usato per leggere registri #
    def read_registers(self, start_address, count):
        if self.connect():
            try:
                response = self.client.read_holding_registers(address=start_address, count=count, slave=self.SLAVE.ID)
                if not response.isError():
                    return response.registers
                else: 
                    logging.warning("Errore nella lettura dei registri.", exc_info=True)
            except Exception as e:
                logging.warning("Exception occurred", exc_info=True)
        else:
            logging.warning("Connessione non riuscita.", exc_info=True)
        return None
    
    """---------------------------DATA INTERACTIONS-----------------------------"""
    
    # def get_mV_main(self):
    #     try:
    #         # Formula: y=mx+q per la correzione lineare #
    #         y = self.DATA.canale_principale_mV*self.banco_di_taratura.m_main + self.banco_di_taratura.q_main
    #         return y
    #     except Exception as e:
    #             logging.warning("Exception occurred", exc_info=True)
                
    def get_V_main(self):
        try:
            # Formula: y=mx+q per la correzione lineare #
            y = self.DATA.canale_principale_mV*self.banco_di_taratura.m_main + self.banco_di_taratura.q_main
            y = y / 1000.0
            return round(y,3)
        except Exception as e:
                logging.warning("Exception occurred measuring mV Main", exc_info=True)
    
    def get_Nm_main(self):
        try:
            # Formula: Nm=(mV-zero)*coeff #
            self.DATA.canale_principale_Nm = (self.get_V_main() - self.DATA.zero_main) * self.DATA.coefficiente_main
            return round(self.DATA.canale_principale_Nm,3)
        except Exception as e:
                logging.warning("Exception occurred measuring Nm", exc_info=True)
    
    def get_mV_temp(self):
        try:
            # Formula: y=mx+q per la correzione lineare #
            y = self.DATA.canale_temperatura_mV*self.banco_di_taratura.m_temp + self.banco_di_taratura.q_temp
            return y
        except Exception as e:
                logging.warning("Exception occurred measuring mV temp", exc_info=True)
    
    def get_C_temp(self):
        try:
            # Formula: C=(mV-zero)*coeff #
            self.DATA.canale_temperatura_C = (self.get_mV_temp()/1000 - self.DATA.zero_temp) * (self.DATA.coefficiente_temp)
            return self.DATA.canale_temperatura_C
        except Exception as e:
                logging.warning("Exception occurred measuring Celsius", exc_info=True)
            
if __name__ == "__main__":
    controller=Controller_MODBUS()
    controller.DATA.canale_principale_mV = controller.read_registers(start_address=16, count=1)
    test=controller.read_registers(start_address=24, count=6)
    print(f"Registri letti: {controller.DATA.canale_principale_mV}")
    print(f"Registri letti normalizzati: {test}")
    
        