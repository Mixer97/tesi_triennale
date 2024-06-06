import Controller_Client_TCP as Controller_Client_TCP
from time import sleep

def main(no):

    if(no==1): # Lettura Cargo
        Controller_Client_TCP.WORKING.read_holding_registers_cargo()  

    elif(no==2): # Lettura mV
        while(True):
            res=Controller_Client_TCP.WORKING.read_holding_registers_mV()        # Work in progress
            print("Risultato: " + str(res))
            
    elif(no==3): # Lettura SR
        Controller_Client_TCP.WORKING.read_status_register()

    elif(no==4): # !!!
        Controller_Client_TCP.TESTING.read_instrument_status()

    elif(no==5):

        Controller_Client_TCP.WORKING.teoretical_calibration_write(1000)
        Controller_Client_TCP.WORKING.teoretical_calibration_read()

    elif(no==6):
        Controller_Client_TCP.WORKING.test_conversione(600000000) #wORKING

    elif(no==7):
        # Controller_Client_TCP.WORKING.teoretical_equalization([0,2.0203,0,1]) #WORKING
        Controller_Client_TCP.WORKING.tara_reset() #WORKING

    elif(no==8):
        Controller_Client_TCP.WORKING.read_sensibility(1) #WORKING
        Controller_Client_TCP.WORKING.read_sensibility(2)
        Controller_Client_TCP.WORKING.read_sensibility(3)
        Controller_Client_TCP.WORKING.read_sensibility(4)
        
    elif(no==9):
        Controller_Client_TCP.WORKING.read_channels_active()

    elif(no==10):
        Controller_Client_TCP.WORKING.set_channel_status([1,0,1,0]) # canale da cambiare [ 4 ... 1 ]
        
    elif(no==11):
        Controller_Client_TCP.UTILS.write_CMDR(Controller_Client_TCP.CMDR_COMMANDS.COMMAND_6902)
        risultatimV=Controller_Client_TCP.client.read_holding_registers(address=52, count=24, slave=Controller_Client_TCP.SLAVE.ID)
        print(risultatimV.registers)
        Controller_Client_TCP.UTILS.write_CMDR(Controller_Client_TCP.CMDR_COMMANDS.COMMAND_6903)
        
    elif(no==12):
        Controller_Client_TCP.TESTING.semiautomatic_tara_deactivation()
        
            
        
    elif(no==666):
        while True:
            Controller_Client_TCP.TESTING.read_HIGHRES_divisions() #INCASINA TUTTO, CAPIRE PERCHE'!

    else:
        print("Out of bounds.")

main(10)
