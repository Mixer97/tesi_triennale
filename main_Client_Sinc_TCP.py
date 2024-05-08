import client_Sinc_TCP
from time import sleep

def main(no):

    if(no==1): # Lettura Cargo
        client_Sinc_TCP.WORKING.read_holding_registers_cargo()  

    elif(no==2): # Lettura mV
        while(True):
            res=client_Sinc_TCP.WORKING.read_holding_registers_mV()        # Work in progress
            # print("Risultato: "  + str(res))
            
    elif(no==3): # Lettura SR
        client_Sinc_TCP.TESTING.read_status_register()

    elif(no==4): # !!!
        client_Sinc_TCP.TESTING.read_instrument_status()

    elif(no==5):
        client_Sinc_TCP.TESTING.teoretical_calibration_read()
        # client_Sinc_TCP.TESTING.teoretical_calibration_write()

    elif(no==6):
        client_Sinc_TCP.WORKING.test_conversione(40000) #wORKING

    elif(no==7):
        client_Sinc_TCP.WORKING.teoretical_equalization([0,0,2,0]) #WORKING
        client_Sinc_TCP.WORKING.tara_reset() #WORKING

    elif(no==8):
        client_Sinc_TCP.WORKING.read_sensibility(1) #WORKING
        client_Sinc_TCP.WORKING.read_sensibility(2)
        client_Sinc_TCP.WORKING.read_sensibility(3)
        client_Sinc_TCP.WORKING.read_sensibility(4)

    elif(no==9):
        client_Sinc_TCP.WORKING.read_channels_active()

    elif(no==10):
        client_Sinc_TCP.WORKING.write_channels_active(4) # Valore da inserire in base 10 (i canali sono da six a dex in binario)

    elif(no==666):
        while True:
            client_Sinc_TCP.TESTING.read_HIGHRES_divisions() #INCASINA TUTTO, CAPIRE PERCHE'!

    else:
        print("Out of bounds.")

main(2)
