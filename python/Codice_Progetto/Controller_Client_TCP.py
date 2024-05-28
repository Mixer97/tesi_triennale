from time import sleep
from pymodbus.client import ModbusTcpClient
from pymodbus.framer import Framer
import View_QT

class SLAVE:
    ID=1
    IP="10.2.0.170"
    PORT=10001
    BAUDRATE=9600
    TIMEOUT=5

#ricordarsi che l'address potrebbe essere (numero-40001)=x
class ADDRESS:
    CMDR = 5
    REGISTER_SR1 = 6
    REGISTER_1_WR1_high = 50
    REGISTER_2_WR1_low = 51
    REGISTER_3 = 52
    REGISTER_AEXC = 61
    REGISTER_EXC = 63


class CMDR_COMMANDS:
    COMMAND_6902 = 6902
    COMMAND_6903 = 6903
    COMMAND_6808 = 6808
    DISABLE_command_cargo = 6809
    CHANNEL_command_search = 6094
    COMMAND_6563 = 6563
    COMMAND_6564 = 6564
    COMMAND_6703 = 6703
    COMMAND_6704 = 6704
    COMMAND_6575 = 6575
    COMMAND_6576 = 6576
    COMMAND_100 = 100
    COMMAND_25 = 25
    COMMAND_27 = 27
    ENABLE_command_dosage_read = 6803
    COMMAND_6501 = 6501
    COMMAND_6502 = 6502
    COMMAND_7 = 7
    COMMAND_9 = 9
    
class DATA:
    LIST_mV_VALUE = [0,0,0,0]


# Configura il client Modbus (VUOLE COMUNQUE UN FRAMER RTU !!)
client = ModbusTcpClient(host=SLAVE.IP, port=SLAVE.PORT, baudrate=SLAVE.BAUDRATE, timeout=SLAVE.TIMEOUT, framer=Framer.RTU)

# Connessione al dispositivo Modbus
connection = client.connect()


class NOT_WORKING:
    x = 0
    
    
    
class WORKING:

    def read_holding_registers_mV():
        if connection:     
                
            # Inviare il comando 6902 a CMDR (abilitare lettura in mV)
            UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_6902)

            # Lettura holding registers (52...55)
            risultatimV=client.read_holding_registers(address=ADDRESS.REGISTER_3, count=4, slave=SLAVE.ID)

            while risultatimV.registers==[0,0,0,0]:
                risultatimV=client.read_holding_registers(address=ADDRESS.REGISTER_3, count=4, slave=SLAVE.ID)

            # Conversione
            for value in range(4):
                risultatimV.registers[value] = float((UTILS.convert_to_signed_16_bit(risultatimV.registers[value]))/100)

            # Print
            # if not risultatimV.isError():
            #     print("Valore letto:", risultatimV.registers)
            # else:
            #         print("Errore nella lettura:", risultatimV)

            # Inviare il comando 6903 a CMDR (disabilitare lettura in mV)
            UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_6903)
            
            return risultatimV.registers

        else:
            print("Impossibile connettersi al dispositivo Modbus")

    def test_conversione(valore_input):
        list = UTILS.value_to_HL(valore_input)

        # Scrivere un valore che puo stare solo in 2 registri per testare
        client.write_registers(address=ADDRESS.REGISTER_1_WR1_high, values=list[0], slave=SLAVE.ID)
        client.write_registers(address=ADDRESS.REGISTER_2_WR1_low, values=list[1], slave=SLAVE.ID)

        # Lettura holding registri high e low
        risultati=client.read_holding_registers(address=ADDRESS.REGISTER_1_WR1_high, count=2, slave=SLAVE.ID)
        risultato_elaborato = (risultati.registers[0] << 16) | risultati.registers[1]
        print("Valore letto: ", risultato_elaborato)

    def teoretical_equalization(list_sensib=[0,0,0,0]): # OSS: indice del canale fra 1 e 4

        for tmp in range(4):

            # Scrittura indice del canale in W1
            x = tmp + 1
            UTILS.write_W1(x)

            # Invio del comando 6703 a CMDR
            UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_6703)

            # Conversione
            list_sensib[tmp] = list_sensib[tmp]*100000

            # Scrittura sensibilità in W1
            UTILS.write_W1(list_sensib[tmp])

            # Invio del comando 6563 a CMDR
            UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_6563)  

        # Conclusione equalizzazione teorica
        UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_6704)
        sleep(1)

        exc_aexc=UTILS.read_EXC_AEXC()

        if (exc_aexc[0] == CMDR_COMMANDS.COMMAND_6704 and exc_aexc[1] == 0):
            print("Equalizzazione conclusa con successo!")
        else:
            print("Equalizzazione fallita. Riprovare.")
              
    def read_sensibility(chn_index): # OSS: indice del canale fra 1 e 4
    
        # Scrittura indice del canale in W1
        UTILS.write_W1(chn_index)

        # Invio del comando 6564 a CMDR
        UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_6564)

        # Lettura del registro R1
        sens = UTILS.read_R1()

        # Conversione
        sens = sens/100000

        print("Sensibilità canale " + str(chn_index) + " = " + str(sens) + " mV/V")

    def tara_reset():

        x = UTILS.read_EXC_AEXC()

        # Azzeramento della Tara
        UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_100)   
        
        # Azzeramento offset in mV   

        x = UTILS.read_EXC_AEXC()

    def write_channels_active(ACR): # IL VALORE DI ACR DEVE ESSERE IN BASE 10

        # Scrittura di ACR in W1
        UTILS.write_W1(ACR)

        # Invio del comando 6575 a CMDR
        UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_6575)

        # Messaggio di conferma
        print("Risultato binario: " + str(ACR))

    def read_channels_active():

        # Invio del comando 6576 a CMDR
        UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_6576)

        # Lettura dei canali attivi in R1
        res=UTILS.read_R1()

        tmp = bin(res).replace("0b", "")
        print("Canali attivi: " + str(tmp))
        
    def read_holding_registers_cargo():
        if connection:     

                # Scrivere il tipo di percentuale carico in W1
                write_result=client.write_registers(address=ADDRESS.REGISTER_2_WR1_low, values=1, slave=SLAVE.ID)
                while write_result.isError():
                    write_result=client.write_registers(address=ADDRESS.REGISTER_2_WR1_low, values=1, slave=SLAVE.ID)

                # Inviare il comando 6808 a CMDR
                UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_6808)
                    
                    
                # Lettura holding registers (52...55)
                risultati_cargo=client.read_holding_registers(address=ADDRESS.REGISTER_3, count=4, slave=SLAVE.ID)
                while risultati_cargo.isError():
                    risultati_cargo=client.read_holding_registers(address=ADDRESS.REGISTER_3, count=4, slave=SLAVE.ID)

                # Conversione
                for value in range(4):
                    risultati_cargo.registers[value] = (UTILS.convert_to_signed_16_bit(risultati_cargo.registers[value]))/10

                # Print
                if not risultati_cargo.isError():
                    print("Valore letto:", risultati_cargo.registers)
                else:
                    print("Errore nella lettura:", risultati_cargo)

        else:
            print("Impossibile connettersi al dispositivo Modbus")

    def read_status_register():
            # Lettura status register (6)
            risultati_SR1=client.read_holding_registers(address=ADDRESS.REGISTER_SR1, count=1, slave=SLAVE.ID)
            while risultati_SR1.isError():
                risultati_SR1=client.read_holding_registers(address=ADDRESS.REGISTER_SR1, count=1, slave=SLAVE.ID)

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

    def teoretical_calibration_write(full_scale):
        # Scrivere il valore del fondo scala in W1
            UTILS.write_W1(full_scale)

        # Inviare il comando 6501 a CMDR
            UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_6501)
        
    def teoretical_calibration_read():
        # Inviare il comando 6502 a CMDR
        UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_6502)
        
        # Lettura del valore di fondo scala in R1
        risultati_fullScale = UTILS.read_R1()

        # Print
        print("Fondoscala = " + str(risultati_fullScale))


class TESTING:
    
    def semiautomatic_tara_activation():
        # Inviare il comando 7 a CMDR
        UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_7)
        
    def semiautomatic_tara_deactivation():
        # Inviare il comando 9 a CMDR
        UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_9)
        
    def automatic_search_of_active_channels(): # CAPIRE COSA FA
        # Inviare il comando 6094 a CMDR
        write_result=client.write_registers(address=ADDRESS.CMDR, values=CMDR_COMMANDS.CHANNEL_command_search, slave=SLAVE.ID)
        while write_result.isError():
            write_result=client.write_registers(address=ADDRESS.CMDR, values=CMDR_COMMANDS.CHANNEL_command_search, slave=SLAVE.ID)

    def read_instrument_status():
        # Inviare il comando 6803 a CMDR
        write_result=client.write_registers(address=ADDRESS.CMDR, values=CMDR_COMMANDS.ENABLE_command_dosage_read, slave=SLAVE.ID)
        while write_result.isError():
            write_result=client.write_registers(address=ADDRESS.CMDR, values=CMDR_COMMANDS.ENABLE_command_dosage_read, slave=SLAVE.ID)

        # Lettura register R1
        risultati_BIS=client.read_holding_registers(address=ADDRESS.REGISTER_1_WR1_high, count=2, slave=SLAVE.ID)
        while risultati_BIS.isError():
            risultati_BIS=client.read_holding_registers(address=ADDRESS.REGISTER_1_WR1_high, count=2, slave=SLAVE.ID)

        # Print
        if not risultati_BIS.isError():
            print("Valore letto:", risultati_BIS.registers)
        else:
            print("Errore nella lettura:", risultati_BIS)

    def read_HIGHRES_divisions():

                # Invio del comando 25 al CMDR (abilitazione lettura)
                UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_25)

                # Lettura registri (40051 - 40058)
                risultati=client.read_holding_registers(address=ADDRESS.REGISTER_1_WR1_high, count=8, slave=SLAVE.ID)

                risultati_elaborated = [0,0,0,0]

                risultati_elaborated[0] = UTILS.convert_to_signed_32_bit(UTILS.HL_to_value([risultati.registers[0], risultati.registers[1]]))
                risultati_elaborated[1] = UTILS.convert_to_signed_32_bit(UTILS.HL_to_value([risultati.registers[2], risultati.registers[3]]))
                risultati_elaborated[2] = UTILS.convert_to_signed_32_bit(UTILS.HL_to_value([risultati.registers[4], risultati.registers[5]]))
                risultati_elaborated[3] = UTILS.convert_to_signed_32_bit(UTILS.HL_to_value([risultati.registers[6], risultati.registers[7]]))

                #print
                print("Valore letto:", risultati_elaborated)

                # Invio del comando 27 al CMDR (disabilitazione lettura)
                UTILS.write_CMDR(CMDR_COMMANDS.COMMAND_27)




class UTILS:

    def value_to_HL(value): # Used for every value. !!! if < 65535 use only tmp[0] (16bit) !!!
        
        # Conversione in int nel caso value sia float (necessaria per eseguire l'operatore >> correttamente)
        value = int(value)
        tmp = [0,0]

        tmp[0] = value >> 16      # high part
        tmp[1] = value & 0xFFFF    # low part

        return tmp
    
    def HL_to_value(list):  # Used for every value.
        result = list[0] << 16 | list[1]
        return result

    def write_CMDR(value):
            
            write_result=client.write_registers(address=ADDRESS.CMDR, values=value, slave=SLAVE.ID)
            while write_result.isError():
                write_result=client.write_registers(address=ADDRESS.CMDR, values=value, slave=SLAVE.ID)

    def write_W1(value):
            
            list = UTILS.value_to_HL(value)

            write_result=client.write_registers(address=ADDRESS.REGISTER_1_WR1_high, values=list[0], slave=SLAVE.ID)
            while write_result.isError():
                write_result=client.write_registers(address=ADDRESS.REGISTER_1_WR1_high, values=list[0], slave=SLAVE.ID)
            
            write_result=client.write_registers(address=ADDRESS.REGISTER_2_WR1_low, values=list[1], slave=SLAVE.ID)
            while write_result.isError():
                write_result=client.write_registers(address=ADDRESS.REGISTER_2_WR1_low, values=list[1], slave=SLAVE.ID)

    def read_R1():

        risultati = client.read_holding_registers(address=ADDRESS.REGISTER_1_WR1_high, count=2, slave=SLAVE.ID)
        while risultati.isError():
            risultati = client.write_registers(address=ADDRESS.REGISTER_1_WR1_high, count=2, slave=SLAVE.ID)
        
        print("high and low: " + str(risultati.registers[0]) + " " + str(risultati.registers[1]))

        risultati_elaborati = UTILS.HL_to_value(risultati.registers)

        return risultati_elaborati

    def read_EXC_AEXC():

        # Lettura AEXC register
        risultati_AEXC=client.read_holding_registers(address=ADDRESS.REGISTER_AEXC, count=1, slave=SLAVE.ID)
        while risultati_AEXC.isError():
            risultati_AEXC=client.read_holding_registers(address=ADDRESS.REGISTER_AEXC, count=1, slave=SLAVE.ID)

        # Lettura EXC register
        risultati_EXC=client.read_holding_registers(address=ADDRESS.REGISTER_EXC, count=1, slave=SLAVE.ID)
        while risultati_EXC.isError():
            risultati_EXC=client.read_holding_registers(address=ADDRESS.REGISTER_EXC, count=1, slave=SLAVE.ID)

        print("Status esecuzione comando: EXC = " + str(risultati_EXC.registers) + ", AEXC = " + str(risultati_AEXC.registers))

        return risultati_EXC.registers[0], risultati_AEXC.registers[0]
    
    def convert_to_signed_32_bit(num):
        # Check if the most significant bit (MSB) is set
        if num & 0x80000000:
            # Perform two's complement conversion
            signed_num = -((num ^ 0xFFFFFFFF) + 1)
        else:
            signed_num = num

        return signed_num

    def convert_to_signed_16_bit(num):
        # Check if the most significant bit (MSB) is set
        if num & 0x8000:
            # Perform two's complement conversion
            signed_num = -((num ^ 0xFFFF) + 1)
        else:
            signed_num = num

        return signed_num




class DATA_INTERACTIONS:
        
    def get_mv():
        return DATA.LIST_mV_VALUE