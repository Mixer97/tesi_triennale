from __future__ import annotations
from typing import TYPE_CHECKING
from time import sleep
from pymodbus.client import ModbusTcpClient
from pymodbus.framer import Framer
import qt_classes.View_QT_HomePage_ui as View_QT_HomePage_ui
from logic_classes.Dialog_error_logic import Error_window
import logging 

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA

class Controller_TCP:
    
    # oggetti slave contengono le informazioni principali per la connessione con il dispositivo #
    class SLAVE:
        def __init__(self, ID, IP, port, baudrate, timeout):
            self.ID=ID
            self.IP=IP
            self.PORT=port
            self.BAUDRATE=baudrate
            self.TIMEOUT=timeout
            self.CHN_VOLTAGE=5

    # address = (numero-40001) #
    class ADDRESS:
        def __init__(self):
            self.CMDR = 5
            self.REGISTER_SR1 = 6
            self.REGISTER_1_WR1_high = 50
            self.REGISTER_2_WR1_low = 51
            self.REGISTER_3 = 52
            self.REGISTER_AEXC = 61
            self.REGISTER_EXC = 63

    # Lista comandi per il registro CMDR #
    class CMDR_COMMANDS:
        def __init__(self):
            self.COMMAND_6902 = 6902
            self.COMMAND_6903 = 6903
            self.COMMAND_6808 = 6808
            self.DISABLE_command_cargo = 6809
            self.CHANNEL_command_search = 6094
            self.COMMAND_6563 = 6563
            self.COMMAND_6564 = 6564
            self.COMMAND_6703 = 6703
            self.COMMAND_6704 = 6704
            self.COMMAND_6575 = 6575
            self.COMMAND_6576 = 6576
            self.COMMAND_100 = 100
            self.COMMAND_25 = 25
            self.COMMAND_27 = 27
            self.ENABLE_command_dosage_read = 6803
            self.COMMAND_6501 = 6501
            self.COMMAND_6502 = 6502
            self.COMMAND_7 = 7
            self.COMMAND_9 = 9
        
    # dati attuali misurati # 
    class DATA:
        def __init__(self):
            self.LIST_mV_VALUE = [0,0,0,0]  #[1,2,3,4] # Aggiornato dal main in un thread separato
            self.LIST_Kg_VALUE = [0,0,0,0]
            self.LIST_Nm_VALUE = [0,0,0,0]
            self.LIST_N_VALUE = [0,0,0,0]
            self.LIST_SENSIBILITY = [1,1,1,1] # settato dalle varie setup pages
            self.LIST_FULLSCALE = [10,10,10,10] # settato dalle varie setup pages
            self.LIST_mV_ZERO = [0,0,0,0] # settato dalle varie setup pages
            self.LEVER_LENGTH = 1 # meters
            self.STATUS_CHANNELS = [0,0,0,0] # settato da setupPage
        
    # costruttore della classe #
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, ID=1, IP="10.2.0.170", port=10001, baudrate=9600, timeout=5):
        self.SLAVE = self.SLAVE(ID, IP, port, baudrate, timeout)
        self.ADDRESS = self.ADDRESS()
        self.CMDR_COMMANDS = self.CMDR_COMMANDS()
        self.DATA = self.DATA()
        self.banco_di_taratura = banco_di_taratura
        self.client = ModbusTcpClient(host=self.SLAVE.IP,
                                      port=self.SLAVE.PORT,
                                      baudrate=self.SLAVE.BAUDRATE,
                                      timeout=self.SLAVE.TIMEOUT,
                                      framer=Framer.RTU)
    
    """---------------------------CONNECT-----------------------------"""

    # Connessione al dispositivo Laumas
    # Metodo usato per connettersi al dispositivo e che riprova fino a 3 volte in caso di perdita di connessione #
    def connect(self):
        try:
            connection = self.client.connect() 
            for i in range(1,4):
                if connection:
                    return True
                else: 
                    logging.error(f"ERROR! connessione al dispostivo presente all'IP {self.SLAVE.IP} fallita.\n tentativo di riconnessione numero: {i}\\3")
                    self.banco_di_taratura.error_window_logic(messaggio_di_errore=f"ERROR! connessione fallita con scheda Laumas, tentativo di riconnessione: {i}\\3\nChiudere la finestra per continuare.")
                    connection = self.client.connect() 
        except Exception as e:
            logging.error("Connessione fallita dopo 3 tentativi!", exc_info=True)
            self.banco_di_taratura.error_window_logic(messaggio_di_errore=f"ERROR! connessione fallita con scheda Laumas, chiudere la finestra\ne riavviare l'applicazione.")
            return False

 
    """---------------------------WORKING-----------------------------"""       
    
    # Metodo che legge i registri da 4053 a 4056 della scheda Laumas #
    def read_holding_registers_mV(self):
            if self.connect:     
                    
                written = False    
                    
                # Inviare il comando 6902 a CMDR (abilitare lettura in mV)
                if not written: 
                    self.write_CMDR(self.CMDR_COMMANDS.COMMAND_6902)
                    written = True
                
                # Lettura holding registers (52...55)
                risultatimV=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_3, count=4, slave=self.SLAVE.ID)

                # Check che tutti i canali NON siano zero (utile all'accensione)
                while risultatimV.registers==[0,0,0,0]:
                    risultatimV=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_3, count=4, slave=self.SLAVE.ID)
                    self.write_CMDR(self.CMDR_COMMANDS.COMMAND_6902)
                    sleep(0.5)

                # Conversione
                for value in range(4):
                    risultatimV.registers[value] = float((self.convert_to_signed_16_bit(risultatimV.registers[value]))/100)

                # Comando di conclusione
                # self.write_CMDR(self.CMDR_COMMANDS.COMMAND_6903)
                
                return risultatimV.registers

            else:
                print("Impossibile connettersi al dispositivo Modbus")
                self.read_holding_registers_mV()

    def test_conversione(self, valore_input):
            list = self.value_to_HL(valore_input)

            # Scrivere un valore che puo stare solo in 2 registri per testare
            self.client.write_registers(address=self.ADDRESS.REGISTER_1_WR1_high, values=list[0], slave=self.SLAVE.ID)
            self.client.write_registers(address=self.ADDRESS.REGISTER_2_WR1_low, values=list[1], slave=self.SLAVE.ID)

            # Lettura holding registri high e low
            risultati=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_1_WR1_high, count=2, slave=self.SLAVE.ID)
            risultato_elaborato = (risultati.registers[0] << 16) | risultati.registers[1]
            print("Valore letto: ", risultato_elaborato)

    def teoretical_equalization(self, list_sensib=[0,0,0,0]): # OSS: indice del canale fra 1 e 4

            for tmp in range(4):

                # Scrittura indice del canale in W1
                x = tmp + 1
                self.write_W1(x)

                # Invio del comando 6703 a CMDR
                self.write_CMDR(self.CMDR_COMMANDS.COMMAND_6703)

                # Conversione
                list_sensib[tmp] = list_sensib[tmp]*100000

                # Scrittura sensibilità in W1
                self.write_W1(list_sensib[tmp])

                # Invio del comando 6563 a CMDR
                self.write_CMDR(self.CMDR_COMMANDS.COMMAND_6563)  

            # Conclusione equalizzazione teorica
            self.write_CMDR(self.CMDR_COMMANDS.COMMAND_6704)
            sleep(1)

            exc_aexc=self.read_EXC_AEXC()

            if (exc_aexc[0] == self.CMDR_COMMANDS.COMMAND_6704 and exc_aexc[1] == 0):
                print("Equalizzazione conclusa con successo!")
            else:
                print("Equalizzazione fallita. Riprovare.")
            
    def read_sensibility(self, chn_index): # OSS: indice del canale fra 1 e 4
        
            # Scrittura indice del canale in W1
            self.write_W1(chn_index)

            # Invio del comando 6564 a CMDR
            self.write_CMDR(self.CMDR_COMMANDS.COMMAND_6564)

            # Lettura del registro R1
            sens = self.read_R1()

            # Conversione
            sens = sens/100000

            print("Sensibilità canale " + str(chn_index) + " = " + str(sens) + " mV/V")

    def tara_reset(self):

            x = self.read_EXC_AEXC()

            # Azzeramento della Tara
            self.write_CMDR(self.CMDR_COMMANDS.COMMAND_100)   
            
            # Azzeramento offset in mV   

            x = self.read_EXC_AEXC()

    def set_channel_status(self, list_status_ch): # IL VALORE DI ACR DEVE ESSERE IN BASE 10
            
            # Calcolo di ACR (numero decimale da inviare alla scheda)
            ACR = 0
            i = 0
            for elements in list_status_ch:
                if list_status_ch[3-i] == 1:
                    ACR = ACR + 2**i
                i=i+1
            print("ACR" + str(ACR))
            # Scrittura di ACR in W1
            self.write_W1(ACR)

            # Invio del comando 6575 a CMDR
            self.write_CMDR(self.CMDR_COMMANDS.COMMAND_6575)
            
            self.read_channels_active()
            
            # Messaggio di conferma
            tmp = bin(ACR).replace("0b", "")
            print("Risultato binario: " + str(tmp))

    def read_channels_active(self):
            """
            Ritorna una lista di 4 elementi nella quale gli 1 rappresentano canali attivi e gli 0 canali disattivi:
            
            ESEMPIO: [0, 1, 0, 1] ⁓ [CH4, CH3, CH2, CH1] --> CH3 e CH1 attivi
            """
            # Invio del comando 6576 a CMDR
            self.write_CMDR(self.CMDR_COMMANDS.COMMAND_6576)
            # Lettura dei canali attivi in R1
            res=self.read_R1()

            channel_status = bin(res).replace("0b", "").zfill(4)
            print("Canali attivi: " + str(channel_status))
            STATUS_CHN = [int(digit) for digit in channel_status]
            print(STATUS_CHN)
            return STATUS_CHN
        
    def read_holding_registers_cargo(self):
            if self.connect:     

                    # Scrivere il tipo di percentuale carico in W1
                    write_result=self.client.write_registers(address=self.ADDRESS.REGISTER_2_WR1_low, values=1, slave=self.SLAVE.ID)
                    while write_result.isError():
                        write_result=self.client.write_registers(address=self.ADDRESS.REGISTER_2_WR1_low, values=1, slave=self.SLAVE.ID)

                    # Inviare il comando 6808 a CMDR
                    self.write_CMDR(self.CMDR_COMMANDS.COMMAND_6808)
                        
                        
                    # Lettura holding registers (52...55)
                    risultati_cargo=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_3, count=4, slave=self.SLAVE.ID)
                    while risultati_cargo.isError():
                        risultati_cargo=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_3, count=4, slave=self.SLAVE.ID)

                    # Conversione
                    for value in range(4):
                        risultati_cargo.registers[value] = (self.convert_to_signed_16_bit(risultati_cargo.registers[value]))/10

                    # Print
                    if not risultati_cargo.isError():
                        print("Valore letto:", risultati_cargo.registers)
                    else:
                        print("Errore nella lettura:", risultati_cargo)

            else:
                print("Impossibile connettersi al dispositivo Modbus")

    def read_status_register(self):
                # Lettura status register (6)
                risultati_SR1=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_SR1, count=1, slave=self.SLAVE.ID)
                while risultati_SR1.isError():
                    risultati_SR1=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_SR1, count=1, slave=self.SLAVE.ID)

                if not risultati_SR1.isError():

                    decimal = risultati_SR1.registers[0]

                    def risultati_SR1_to_binary(decimal):   # Convertitore decimale-binario
                        binary = ""
                        if decimal == 0:
                            return "0"
                        while decimal > 0:
                            remainder = decimal % 2
                            binary = str(remainder) + binary
                            decimal = decimal // 2
                        return binary
                                
                    def find_set_bits(binary):
                        set_bits = []
                        for i, bit in enumerate(binary):
                            if bit == '1':
                                set_bits.append(15 - i)  # Calcoliamo l'indice partendo dal bit più significativo
                        return set_bits
                        
                    bit_impostati_a_1 = find_set_bits(risultati_SR1_to_binary(decimal))
                    print("I seguenti bit sono impostati su 1:", bit_impostati_a_1)      # Print

                    print("Valore letto:", risultati_SR1.registers)
                else:
                    print("Errore nella lettura:", risultati_SR1)

    def teoretical_calibration_write(self, full_scale):
            # Scrivere il valore del fondo scala in W1
                self.write_W1(full_scale)

            # Inviare il comando 6501 a CMDR
                self.write_CMDR(self.CMDR_COMMANDS.COMMAND_6501)
        
    def teoretical_calibration_read(self):
            # Inviare il comando 6502 a CMDR
            self.write_CMDR(self.CMDR_COMMANDS.COMMAND_6502)
            
            # Lettura del valore di fondo scala in R1
            risultati_fullScale = self.read_R1()

            # Print
            print("Fondoscala = " + str(risultati_fullScale))


    """---------------------------TESTING-----------------------------"""
        
    def semiautomatic_tara_activation(self):
            # Inviare il comando 7 a CMDR
            self.write_CMDR(self.CMDR_COMMANDS.COMMAND_7)
        
    def semiautomatic_tara_deactivation(self):
            # Inviare il comando 9 a CMDR
            self.write_CMDR(self.CMDR_COMMANDS.COMMAND_9)
        
    def automatic_search_of_active_channels(self): # CAPIRE COSA FA
            # Inviare il comando 6094 a CMDR
            write_result=self.client.write_registers(address=self.ADDRESS.CMDR, values=self.CMDR_COMMANDS.CHANNEL_command_search, slave=self.SLAVE.ID)
            while write_result.isError():
                write_result=self.client.write_registers(address=self.ADDRESS.CMDR, values=self.CMDR_COMMANDS.CHANNEL_command_search, slave=self.SLAVE.ID)
    
    def read_instrument_status(self):
            # Inviare il comando 6803 a CMDR
            write_result=self.client.write_registers(address=self.ADDRESS.CMDR, values=self.CMDR_COMMANDS.ENABLE_command_dosage_read, slave=self.SLAVE.ID)
            while write_result.isError():
                write_result=self.client.write_registers(address=self.ADDRESS.CMDR, values=self.CMDR_COMMANDS.ENABLE_command_dosage_read, slave=self.SLAVE.ID)

            # Lettura register R1
            risultati_BIS=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_1_WR1_high, count=2, slave=self.SLAVE.ID)
            while risultati_BIS.isError():
                risultati_BIS=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_1_WR1_high, count=2, slave=self.SLAVE.ID)

            # Print
            if not risultati_BIS.isError():
                print("Valore letto:", risultati_BIS.registers)
            else:
                print("Errore nella lettura:", risultati_BIS)
    
    def read_HIGHRES_divisions(self):

                    # Invio del comando 25 al CMDR (abilitazione lettura)
                    self.write_CMDR(self.CMDR_COMMANDS.COMMAND_25)

                    # Lettura registri (40051 - 40058)
                    risultati=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_1_WR1_high, count=8, slave=self.SLAVE.ID)

                    risultati_elaborated = [0,0,0,0]

                    risultati_elaborated[0] = self.convert_to_signed_32_bit(self.HL_to_value([risultati.registers[0], risultati.registers[1]]))
                    risultati_elaborated[1] = self.convert_to_signed_32_bit(self.HL_to_value([risultati.registers[2], risultati.registers[3]]))
                    risultati_elaborated[2] = self.convert_to_signed_32_bit(self.HL_to_value([risultati.registers[4], risultati.registers[5]]))
                    risultati_elaborated[3] = self.convert_to_signed_32_bit(self.HL_to_value([risultati.registers[6], risultati.registers[7]]))

                    #print
                    print("Valore letto:", risultati_elaborated)

                    # Invio del comando 27 al CMDR (disabilitazione lettura)
                    self.write_CMDR(self.CMDR_COMMANDS.COMMAND_27)




    """---------------------------UTILS-----------------------------"""

    def value_to_HL(self, value): # Used for every value. !!! if < 65535 use only tmp[0] (16bit) !!!
            
            # Conversione in int nel caso value sia float (necessaria per eseguire l'operatore >> correttamente)
            value = int(value)
            tmp = [0,0]

            tmp[0] = value >> 16      # high part
            tmp[1] = value & 0xFFFF    # low part

            return tmp
    
    def HL_to_value(self, list):  # Used for every value.
            result = list[0] << 16 | list[1]
            return result
    
    def write_CMDR(self, value):
            
            write_result=self.client.write_registers(address=self.ADDRESS.CMDR, values=value, slave=self.SLAVE.ID)
            while write_result.isError():
                write_result=self.client.write_registers(address=self.ADDRESS.CMDR, values=value, slave=self.SLAVE.ID)
    
    def write_W1(self, value):
        """
        Metodo usato per SCRIVERE nei due registri High e Low un certo valore inserito in value = . . .
        """
        if self.connect:        
            list = self.value_to_HL(value)
            
            write_result=self.client.write_registers(address=self.ADDRESS.REGISTER_1_WR1_high, values=list[0], slave=self.SLAVE.ID)
            while write_result.isError():
                write_result=self.client.write_registers(address=self.ADDRESS.REGISTER_1_WR1_high, values=list[0], slave=self.SLAVE.ID)
            
            write_result=self.client.write_registers(address=self.ADDRESS.REGISTER_2_WR1_low, values=list[1], slave=self.SLAVE.ID)
            while write_result.isError():
                write_result=self.client.write_registers(address=self.ADDRESS.REGISTER_2_WR1_low, values=list[1], slave=self.SLAVE.ID)
    
        else:
            print("Errore nella scrittura di W1")
            sleep(1)
            self.write_W1()
        
    def read_R1(self):
        """
        Metodo usato per LEGGERE nei due registri High e Low per poi tornare un valore
        """
        if self.connect:
            risultati = self.client.read_holding_registers(address=self.ADDRESS.REGISTER_1_WR1_high, count=2, slave=self.SLAVE.ID)
            while risultati.isError():
                risultati = self.client.read_holding_registers(address=self.ADDRESS.REGISTER_1_WR1_high, count=2, slave=self.SLAVE.ID)
            
            # print("high and low: " + str(risultati.registers[0]) + " " + str(risultati.registers[1]))

            risultati_elaborati = self.HL_to_value(risultati.registers)

            return risultati_elaborati
        else:
            print("Errore nella lettura di R1")
            sleep(1)
            self.read_R1()
    
    def read_EXC_AEXC(self):

            # Lettura AEXC register
            risultati_AEXC=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_AEXC, count=1, slave=self.SLAVE.ID)
            while risultati_AEXC.isError():
                risultati_AEXC=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_AEXC, count=1, slave=self.SLAVE.ID)

            # Lettura EXC register
            risultati_EXC=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_EXC, count=1, slave=self.SLAVE.ID)
            while risultati_EXC.isError():
                risultati_EXC=self.client.read_holding_registers(address=self.ADDRESS.REGISTER_EXC, count=1, slave=self.SLAVE.ID)

            print("Status esecuzione comando: EXC = " + str(risultati_EXC.registers) + ", AEXC = " + str(risultati_AEXC.registers))

            return risultati_EXC.registers[0], risultati_AEXC.registers[0]
    
    def convert_to_signed_32_bit(self, num):
            # Check if the most significant bit (MSB) is set
            if num & 0x80000000:
                # Perform two's complement conversion
                signed_num = -((num ^ 0xFFFFFFFF) + 1)
            else:
                signed_num = num

            return signed_num
    
    def convert_to_signed_16_bit(self, num):
            # Check if the most significant bit (MSB) is set
            if num & 0x8000:
                # Perform two's complement conversion
                signed_num = -((num ^ 0xFFFF) + 1)
            else:
                signed_num = num

            return signed_num




    """---------------------------DATA INTERACTIONS-----------------------------"""
            
    def get_mv(self):
        """
        Ritorna una lista espressa in mV di 4 elementi: [CH1, CH2, CH3, CH4]
        """
        return self.DATA.LIST_mV_VALUE
    
    def get_Kg(self):
        """
        Ritorna una lista espressa in Kg di 4 elementi: [CH1, CH2, CH3, CH4]
        """
        i = 0
        for i in range(0, len(self.DATA.LIST_mV_VALUE)):
            if self.DATA.LIST_SENSIBILITY[i]!=0:
                self.DATA.LIST_Kg_VALUE[i] = abs((self.DATA.LIST_FULLSCALE[i]/(self.SLAVE.CHN_VOLTAGE*self.DATA.LIST_SENSIBILITY[i]))*(self.DATA.LIST_mV_VALUE[i] - self.DATA.LIST_mV_ZERO[i]))/9.81
            else:
                self.DATA.LIST_Kg_VALUE[i] = 0
        return self.DATA.LIST_Kg_VALUE
    
    def get_Nm(self, lever_length=1):
        """
        Ritorna una lista espressa in Nm di 4 elementi: [CH1, CH2, CH3, CH4]
        """
        i = 0
        for i in range(0, len(self.DATA.LIST_mV_VALUE)):
            self.DATA.LEVER_LENGTH = lever_length
            if self.DATA.LIST_SENSIBILITY[i]!=0:
                self.DATA.LIST_Nm_VALUE[i] = self.DATA.LEVER_LENGTH*(self.DATA.LIST_FULLSCALE[i]/(self.SLAVE.CHN_VOLTAGE*self.DATA.LIST_SENSIBILITY[i]))*(self.DATA.LIST_mV_VALUE[i] - self.DATA.LIST_mV_ZERO[i])
            else:
                self.DATA.LIST_Nm_VALUE[i] = 0
        return self.DATA.LIST_Nm_VALUE
        
    def get_N(self):
        """
        Ritorna una lista espressa in N di 4 elementi: [CH1, CH2, CH3, CH4]
        """
        i = 0
        for i in range(0, len(self.DATA.LIST_mV_VALUE)):
            if self.DATA.LIST_SENSIBILITY[i]!=0:
                self.DATA.LIST_N_VALUE[i] = (self.DATA.LIST_FULLSCALE[i]/(self.SLAVE.CHN_VOLTAGE*self.DATA.LIST_SENSIBILITY[i]))*(self.DATA.LIST_mV_VALUE[i] - self.DATA.LIST_mV_ZERO[i])
            else:
                self.DATA.LIST_N_VALUE[i] = 0
        return self.DATA.LIST_N_VALUE
    
    def setup_full_update(self, list):
        """
        Setta i canali attivi sulla Laumas in accordo con la lista immessa:
        
        ESEMPIO: [0, 1, 0, 1] ⁓ [CH4, CH3, CH2, CH1] --> CH3 e CH1 attivi
        """
        print(list)
        self.set_channel_status(list)
        
        