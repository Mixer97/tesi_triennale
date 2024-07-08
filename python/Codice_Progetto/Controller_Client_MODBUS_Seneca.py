from pymodbus.client import ModbusSerialClient
from pymodbus.framer import Framer
from pymodbus import pymodbus_apply_logging_config
from time import sleep
import sys
import serial

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
            self.canale_principale_mV=0
            self.canale_principale_Nm=0
            self.zero_main=0
            self.coefficiente_main = 1  # Nm/mV
            
            # temp
            self.canale_temperatura_mV=0
            self.canale_temperatura_C=0
            self.zero_temp=0
            self.coefficiente_temp = 1  # C/mV
            
    def __init__(self, port="COM8", baudrate=2400, bytesize=8, parity="N", stopbits=1, ID=1):
        self.SLAVE = self.SLAVE(port, baudrate, bytesize, parity, stopbits, ID)
        self.DATA = self.DATA()
        self.client = ModbusSerialClient(
            method='rtu',
            port=self.SLAVE.port,
            baudrate=self.SLAVE.baudrate,
            bytesize=self.SLAVE.bytesize,
            parity=self.SLAVE.parity,
            stopbits=self.SLAVE.stopbits
        )

    """---------------------------CONNECT-----------------------------"""

    def connect(self):
        
        connection = self.client.connect() 
        for i in range(1,11):
            if connection:
                return True
            else: 
                print(f"ERROR! connessione al dispostivo presente sulla COM-port {self.SLAVE.port} fallita.\n tentativo di riconnessione numero: {i}\\10")
                connection = self.client.connect() 
                sleep(0.5)
        print("Connessione fallita dopo 10 tentativi!")
        return False

    """---------------------------WORKING-----------------------------"""      
        
    def read_MachineID(self):
        risultati = self.client.read_holding_registers(address=0, count=1, slave=self.SLAVE.ID)
        while risultati.isError():
            risultati = self.client.read_holding_registers(address=0, count=1, slave=self.SLAVE.ID)
        risultati_elaborati = risultati
        return risultati_elaborati
    
    
    def read_holding_registers_mV(self):
        list_results_mV = [0,0]
        while list_results_mV == [0,0]:
            list_results_mV = self.read_registers(start_address=16, count=2)
        return list_results_mV
            
    """---------------------------UTILS-----------------------------"""
    
     
    def read_registers(self, start_address, count):
        if self.connect():
            try:
                response = self.client.read_holding_registers(address=start_address, count=count, slave=self.SLAVE.ID)
                if not response.isError():
                    return response.registers
                else:
                    print("Errore nella lettura dei registri.")
            except Exception as e:
                print(f"Eccezione durante la lettura dei registri: {e}")
        else:
            print("Connessione non riuscita.")
        return None
    
    """---------------------------DATA INTERACTIONS-----------------------------"""
    
    def get_mV_main(self):
        return self.DATA.canale_principale_mV
    
    def get_Nm_main(self):
        self.DATA.canale_principale_Nm = (self.DATA.canale_principale_mV - self.DATA.zero_main) * self.DATA.coefficiente_main
        return self.DATA.canale_principale_Nm
    
    def get_mV_temp(self):
        return self.DATA.canale_temperatura_mV
    
    def get_C_temp(self):
        self.DATA.canale_temperatura_C = (self.DATA.canale_temperatura_mV - self.DATA.zero_temp) * self.DATA.coefficiente_temp
        return self.DATA.canale_temperatura_C
            
if __name__ == "__main__":
    controller=Controller_MODBUS()
    controller.DATA.canale_principale_mV = controller.read_registers(start_address=16, count=1)
    test=controller.read_registers(start_address=24, count=6)
    print(f"Registri letti: {controller.DATA.canale_principale_mV}")
    print(f"Registri letti normalizzati: {test}")
    
        