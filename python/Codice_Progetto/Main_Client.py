import Controller_Client_TCP_Laumas as Controller_Client_TCP_Laumas
from time import sleep

def main(no):

    if(no==1): # Lettura Cargo
        controller_tcp.read_holding_registers_cargo()  

    elif(no==2): # Lettura mV
        while(True):
            res=controller_tcp.read_holding_registers_mV()        # Work in progress
            print("Risultato: " + str(res))
            
    elif(no==3): # Lettura SR
        controller_tcp.read_status_register()

    elif(no==4): # !!!
        controller_tcp.read_instrument_status()

    elif(no==5):

        controller_tcp.teoretical_calibration_write(1000)
        controller_tcp.teoretical_calibration_read()

    elif(no==6):
        controller_tcp.test_conversione(600000000) #wORKING

    elif(no==7):
        # Controller_Client_TCP.WORKING.teoretical_equalization([0,2.0203,0,1]) #WORKING
        controller_tcp.tara_reset() #WORKING

    elif(no==8):
        controller_tcp.read_sensibility(1) #WORKING
        controller_tcp.read_sensibility(2)
        controller_tcp.read_sensibility(3)
        controller_tcp.read_sensibility(4)
        
    elif(no==9):
        controller_tcp.read_channels_active()

    elif(no==10):
        controller_tcp.set_channel_status([1,0,1,0]) # canale da cambiare [ 4 ... 1 ]
        
    elif(no==11):
        controller_tcp.write_CMDR(controller_tcp.CMDR_COMMANDS.COMMAND_6902)
        risultatimV=controller_tcp.client.read_holding_registers(address=52, count=24, slave=controller_tcp.SLAVE.ID)
        print(risultatimV.registers)
        controller_tcp.write_CMDR(controller_tcp.CMDR_COMMANDS.COMMAND_6903)
        
    elif(no==12):
        controller_tcp.semiautomatic_tara_deactivation()
        
            
        
    elif(no==666):
        while True:
            controller_tcp.read_HIGHRES_divisions() #INCASINA TUTTO, CAPIRE PERCHE'!

    else:
        print("Out of bounds.")

controller_tcp=Controller_Client_TCP_Laumas.Controller_TCP()
main(2)
