from pymodbus.client import ModbusSerialClient
from pymodbus.framer import Framer
from pymodbus import pymodbus_apply_logging_config
from time import sleep
import sys

# print(sys.prefix)

class SLAVE:
    port="COM4"
    baudrate=38400
    bytesize=8
    parity="N"
    stopbits=1
    ID=1
   
client = ModbusSerialClient(method='rtu', port=SLAVE.port, baudrate=SLAVE.baudrate, bytesize=SLAVE.bytesize, parity=SLAVE.parity, stopbits=SLAVE.stopbits)
connection = client.connect()   

def run():
    
    for i in range(1,11):
        if connection:
                break
        else: 
            print(f"ERROR! connessione al dispostivo presente sulla COM-port {SLAVE.port} fallita.\n tentativo di riconnessione numero: {i}\\10")
            sleep(0.5)
        exit()

class TESTING:
    
   def read_MachineID():

        risultati = client.read_holding_registers(address=40001, count=1, slave=SLAVE.ID)
        while risultati.isError():
            risultati = client.read_holding_registers(address=40001, count=1, slave=SLAVE.ID)
        
        # print("high and low: " + str(risultati.registers[0]) + " " + str(risultati.registers[1]))

        risultati_elaborati = risultati

        return risultati_elaborati



if __name__ == "__main__":
    run()
    print("Connessione avvenuta con successo!")
    # print(TESTING.read_MachineID())
    res=client.read_input_registers(0, 2, 1)
    print(res)