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
        
            # status canale
            self.status_canali_SG600=0
            
            # main
            self.canale_principale_mV=0
            self.canale_principale_Nm=0
            self.canale_principale_Kg=0
            self.canale_principale_N=0
            self.sensibilità_principale=2.0000
            self.fondo_scala_principale=10000
            self.lever_length=1
            self.zero_main=0
            
            # temp
            self.canale_temperatura_mV=0
            self.canale_temperatura_C=0
            self.sensibilità_temperatura=1
            self.fondo_scala_temperatura=1
            self.zero_temp=0
            
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
        # print("high and low: " + str(risultati.registers[0]) + " " + str(risultati.registers[1]))
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
    
    # def get_Nm_main(self):
    #     if self.DATA.sensibilità_principale!=0:
    #         self.DATA.canale_principale_Nm = self.DATA.lever_length*9.81*(self.DATA.fondo_scala_principale/(self.SLAVE.CHN_VOLTAGE*self.DATA.LIST_SENSIBILITY[i]))*(self.DATA.LIST_mV_ZERO[i] - self.DATA.LIST_mV_VALUE[i])
    #     else:
    #         self.DATA.LIST_Nm_VALUE[i] = 0
    #     return self.DATA.LIST_Nm_VALUE
    
    def get_mV_temp(self):
        return self.DATA.canale_temperatura_mV
    
    # def get_C_temp():
    #     return DATA.canale_temperatura_C
            
if __name__ == "__main__":
    controller=Controller_MODBUS()
    controller.DATA.canale_principale_mV = controller.read_registers(start_address=16, count=1)
    test=controller.read_registers(start_address=24, count=6)
    print(f"Registri letti: {controller.DATA.canale_principale_mV}")
    print(f"Registri letti normalizzati: {test}")
    
        