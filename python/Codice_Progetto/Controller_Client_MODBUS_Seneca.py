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
            print("Connessione avvenuta con successo.")
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


if __name__ == "__main__":
    # print(TESTING.read_MachineID().registers)
    registers = UTILS.read_registers(start_address=16, count=1)
    print(f"Registri letti: {registers}")
    
    
