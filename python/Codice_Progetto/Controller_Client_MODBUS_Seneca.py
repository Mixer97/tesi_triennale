from pymodbus.client import ModbusSerialClient
from pymodbus.framer import Framer
from pymodbus import pymodbus_apply_logging_config
from time import sleep
import sys
import serial

# print(sys.prefix)

class SLAVE:        # Comunicazione su RS-232
    port="COM8"
    baudrate=2400
    bytesize=8
    parity="N"
    stopbits=1
    ID=1
    
class DATA:
    # status canale
    status_canali_SG600=0
    
    # main
    canale_principale_mV=0
    canale_principale_Nm=0
    sensibilità_principale=2.0000
    fondo_scala_principale=10000
    lever_length=1
    zero_main=0
    
    # temp
    canale_temperatura_mV=0
    canale_temperatura_C=0
    sensibilità_temperatura=0
    fondo_scala_temperatura=0
    zero_temp=0
    

client = ModbusSerialClient(
    method='rtu',
    port=SLAVE.port,
    baudrate=SLAVE.baudrate,
    bytesize=SLAVE.bytesize,
    parity=SLAVE.parity,
    stopbits=SLAVE.stopbits
)

 

def connect():
    
    connection = client.connect() 
    for i in range(1,11):
        if connection:
            return True
        else: 
            print(f"ERROR! connessione al dispostivo presente sulla COM-port {SLAVE.port} fallita.\n tentativo di riconnessione numero: {i}\\10")
            connection = client.connect() 
            sleep(0.5)
    print("Connessione fallita dopo 10 tentativi!")
    return False
                

class TESTING:
    
    def read_MachineID():
        risultati = client.read_holding_registers(address=0, count=1, slave=SLAVE.ID)
        while risultati.isError():
            risultati = client.read_holding_registers(address=0, count=1, slave=SLAVE.ID)
        # print("high and low: " + str(risultati.registers[0]) + " " + str(risultati.registers[1]))
        risultati_elaborati = risultati
        return risultati_elaborati

class WORKING:
    
    def read_holding_registers_mV():
        list_results_mV = [0,0]
        while list_results_mV == [0,0]:
            list_results_mV = UTILS.read_registers(start_address=16, count=2)
        return list_results_mV
            




class UTILS:

    def read_registers(start_address, count):
        if connect():
            try:
                response = client.read_holding_registers(address=start_address, count=count, slave=SLAVE.ID)
                if not response.isError():
                    return response.registers
                else:
                    print("Errore nella lettura dei registri.")
            except Exception as e:
                print(f"Eccezione durante la lettura dei registri: {e}")
        else:
            print("Connessione non riuscita.")
        return None


class DATA_INTERACTIONS:

    def get_mV_main():
        return DATA.canale_principale_mV


    # def get_Nm_main():
    #     if DATA.sensibilità_principale!=0:
    #         DATA.canale_principale_Nm = DATA.lever_length*9.81*(DATA.fondo_scala_principale/(SLAVE.CHN_VOLTAGE*DATA.LIST_SENSIBILITY[i]))*(DATA.LIST_mV_ZERO[i] - DATA.LIST_mV_VALUE[i])
    #     else:
    #         DATA.LIST_Nm_VALUE[i] = 0
    #     return DATA.LIST_Nm_VALUE
    
    def get_mV_temp():
        return DATA.canale_temperatura_mV
    
    # def get_C_temp():
    #     return DATA.canale_temperatura_C
        



if __name__ == "__main__":
    # print(TESTING.read_MachineID().registers)
    DATA.canale_principale_mV = UTILS.read_registers(start_address=16, count=1)
    test=UTILS.read_registers(start_address=24, count=6)
    print(f"Registri letti: {DATA.canale_principale_mV}")
    print(f"Registri letti normalizzati: {test}")
    
    
