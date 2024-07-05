# importing the module 
import pandas as pd 
import Controller_Client_TCP_Laumas as Controller_Client_TCP_Laumas
import Controller_Client_MODBUS_Seneca
import time
from time import sleep
import csv
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
        
class LOGGER:
    
    class DATA:
        def __init__(self):
            self.startStop_logger=False
            self.text_lcd=["mV","mV","mV","mV"]  # Viene aggiornata dalla Main_View in automatico
            self.result_list_1_4=[0,0,0,0]
            self.result_list_SG600_main_temp=[0,0]
            self.text_lcd_SG600_main_temp=["mV","mV"]  # Viene aggiornato dalla Main View in automatico [[DA IMPLEMENTARE]] 
            self.loop_status=True
            self.periodo_logger=0.005
            self.counter_registrazione = 0
    
    def __init__(self, banco_di_taratura, nome_CSV, starting_status=False):
        self.DATA=LOGGER.DATA()
        self.banco_di_taratura = banco_di_taratura
        self.nome_CSV = nome_CSV
        self.path_CSV = 'python\\Codice_Progetto\\CSV\\' + str(self.nome_CSV) + ".csv"
        self.DATA.startStop_logger = starting_status
        self.tmp = None
        
        # Creazione liste per dataframe
        self.list_time = []
        self.list_cella1 = []
        self.list_cella2 = []  
        self.list_cella3 = [] 
        self.list_cella4 = [] 
        self.list_SG600_main = []
        self.list_SG600_temp = []
        self.list_unit_t = []
        self.list_unit_1 = []
        self.list_unit_2 = []
        self.list_unit_3 = []
        self.list_unit_4 = []
        self.list_SG600_main_unit = []
        self.list_SG600_temp_unit = []
        
        
        
        # creating the DataFrame 
        self.my_df = {'Time': self.list_time,
                'unit_Time':self.list_unit_t,  
                'Cella_1': self.list_cella1,
                'unit_1':self.list_unit_1, 
                'Cella_2': self.list_cella2,
                'unit_2':self.list_unit_2, 
                'Cella_3': self.list_cella3,
                'unit_3':self.list_unit_3, 
                'Cella_4': self.list_cella4,  
                'unit_4':self.list_unit_4,
                'SG600_main':self.list_SG600_main,
                'unit_main':self.list_SG600_main_unit,
                'SG600_temp':self.list_SG600_temp,
                'unit_temp':self.list_SG600_temp_unit,} 
        
        self.df = pd.DataFrame(self.my_df) 
        
        self.check_path()
      
            # timer start
        self.timer = 0
        self.start_timer = time.time()  
        
        # Controllare se il file esiste
    def check_path(self):
        if os.path.exists(self.path_CSV):
            print(f"Il file '{self.path_CSV}' esiste già. Non è stato sovrascritto.")
            self.tmp = f"{self.nome_CSV}_{self.DATA.counter_registrazione}"
            self.path_CSV = 'python\\Codice_Progetto\\CSV\\' + str(self.tmp) + ".csv"
            self.DATA.counter_registrazione = self.DATA.counter_registrazione + 1
            self.check_path()
            # pop up con messaggio: inserire un nuovo nome al file di registrazione
        else:
            # Salvare il DataFrame come CSV
            self.df.to_csv(self.path_CSV, index=False)  
            print(f"Il file '{self.path_CSV}' è stato salvato con successo.")
            if self.tmp != None:
                self.nome_CSV = self.tmp
        
          
    def log_data(self, controller_TCP, controller_MODBUS):  
        self.controller_TCP = controller_TCP
        self.controller_MODBUS = controller_MODBUS
        while self.DATA.loop_status:
            sleep(self.DATA.periodo_logger)   # timer per gestire la frequenza di campionamento del logger (frequenza più alta possibile per non avere duplicati)
            if self.DATA.startStop_logger:
                # Processing dei dati
                self.stop_timer = time.time()
                self.timer = self.stop_timer - self.start_timer

                # Aggiornamento logger con unità di misura necessarie
                self.update_CH1(self.controller_TCP)
                self.update_CH2(self.controller_TCP)
                self.update_CH3(self.controller_TCP)
                self.update_CH4(self.controller_TCP)
                self.update_SG600_main(self.controller_MODBUS)
                self.update_SG600_temp(self.controller_MODBUS)
                
                # Scrittura di una riga
                with open(self.path_CSV, mode="a", newline="") as csv_doc:
                    writer = csv.writer(csv_doc)
                    list_to_write = [self.timer,
                                    "s",
                                    self.DATA.result_list_1_4[0],
                                    self.DATA.text_lcd[0],
                                    self.DATA.result_list_1_4[1],
                                    self.DATA.text_lcd[1],
                                    self.DATA.result_list_1_4[2],
                                    self.DATA.text_lcd[2],
                                    self.DATA.result_list_1_4[3],
                                    self.DATA.text_lcd[3],
                                    self.DATA.result_list_SG600_main_temp[0],
                                    self.DATA.text_lcd_SG600_main_temp[0],
                                    self.DATA.result_list_SG600_main_temp[1],
                                    self.DATA.text_lcd_SG600_main_temp[1],
                                    ]
                    
                    writer.writerow(list_to_write)  # Scrittura di una riga del CSV
                    print(list_to_write)    # Print di testing

    def update_CH1(self, controller_TCP):
        if self.DATA.text_lcd[0] == "mV":
                list_mV = Controller_Client_TCP_Laumas.Controller_TCP.get_mv(controller_TCP)
                self.DATA.result_list_1_4[0]=list_mV[0]
        elif self.DATA.text_lcd[0] == "Kg":
                list_Kg = Controller_Client_TCP_Laumas.Controller_TCP.get_Kg(controller_TCP)
                self.DATA.result_list_1_4[0]=list_Kg[0]
        elif self.DATA.text_lcd[0] == "N":
                list_N = Controller_Client_TCP_Laumas.Controller_TCP.get_N(controller_TCP)
                self.DATA.result_list_1_4[0]=list_N[0]
        elif self.DATA.text_lcd[0] == "Nm":
                list_Nm = Controller_Client_TCP_Laumas.Controller_TCP.get_Nm(controller_TCP)
                self.DATA.result_list_1_4[0]=list_Nm[0]
        else:
                print("Error: something went wrong in the selection of the measuring unit in CH1!")       
                exit(1)
                
    def update_CH2(self, controller_TCP):
        if self.DATA.text_lcd[1] == "mV":
                list_mV = Controller_Client_TCP_Laumas.Controller_TCP.get_mv(controller_TCP)
                self.DATA.result_list_1_4[1]=list_mV[1]
        elif self.DATA.text_lcd[1] == "Kg":
                list_Kg = Controller_Client_TCP_Laumas.Controller_TCP.get_Kg(controller_TCP)
                self.DATA.result_list_1_4[1]=list_Kg[1]
        elif self.DATA.text_lcd[1] == "N":
                list_N = Controller_Client_TCP_Laumas.Controller_TCP.get_N(controller_TCP)
                self.DATA.result_list_1_4[1]=list_N[1]
        elif self.DATA.text_lcd[1] == "Nm":
                list_Nm = Controller_Client_TCP_Laumas.Controller_TCP.get_Nm(controller_TCP)
                self.DATA.result_list_1_4[1]=list_Nm[1]
        else:
                print("Error: something went wrong in the selection of the measuring unit in CH2!")       
                exit(1)
                
    def update_CH3(self, controller_TCP):
        if self.DATA.text_lcd[2] == "mV":
                list_mV = Controller_Client_TCP_Laumas.Controller_TCP.get_mv(controller_TCP)
                self.DATA.result_list_1_4[2]=list_mV[2]
        elif self.DATA.text_lcd[2] == "Kg":
                list_Kg = Controller_Client_TCP_Laumas.Controller_TCP.get_Kg(controller_TCP)
                self.DATA.result_list_1_4[2]=list_Kg[2]
        elif self.DATA.text_lcd[2] == "N":
                list_N = Controller_Client_TCP_Laumas.Controller_TCP.get_N(controller_TCP)
                self.DATA.result_list_1_4[2]=list_N[2]
        elif self.DATA.text_lcd[2] == "Nm":
                list_Nm = Controller_Client_TCP_Laumas.Controller_TCP.get_Nm(controller_TCP)
                self.DATA.result_list_1_4[2]=list_Nm[2]
        else:
                print("Error: something went wrong in the selection of the measuring unit in CH3!")       
                exit(1)
                
    def update_CH4(self, controller_TCP):
        if self.DATA.text_lcd[3] == "mV":
                list_mV = Controller_Client_TCP_Laumas.Controller_TCP.get_mv(controller_TCP)
                self.DATA.result_list_1_4[3]=list_mV[3]
        elif self.DATA.text_lcd[3] == "Kg":
                list_Kg = Controller_Client_TCP_Laumas.Controller_TCP.get_Kg(controller_TCP)
                self.DATA.result_list_1_4[3]=list_Kg[3]
        elif self.DATA.text_lcd[3] == "N":
                list_N = Controller_Client_TCP_Laumas.Controller_TCP.get_N(controller_TCP)
                self.DATA.result_list_1_4[3]=list_N[3]
        elif self.DATA.text_lcd[3] == "Nm":
                list_Nm = Controller_Client_TCP_Laumas.Controller_TCP.get_Nm(controller_TCP)
                self.DATA.result_list_1_4[3]=list_Nm[3]
        else:
                print("Error: something went wrong in the selection of the measuring unit in CH4!")       
                exit(1)
                
    def update_SG600_main(self, controller_MODBUS):
        if self.DATA.text_lcd_SG600_main_temp[0] == "mV":
                main_mV = Controller_Client_MODBUS_Seneca.Controller_MODBUS.get_mV_main(controller_MODBUS)
                self.DATA.result_list_SG600_main_temp[0]=main_mV
        elif self.DATA.text_lcd_SG600_main_temp[0] == "Nm":
                main_Nm = Controller_Client_MODBUS_Seneca.Controller_MODBUS.get_Nm_main(controller_MODBUS)
                self.DATA.result_list_SG600_main_temp[0]=main_Nm
        else:
                print("Error: something went wrong in the selection of the measuring unit in SG600 main!")       
                exit(1)
                
    def update_SG600_temp(self, controller_MODBUS):
        if self.DATA.text_lcd_SG600_main_temp[1] == "mV":
                temp_mV = Controller_Client_MODBUS_Seneca.Controller_MODBUS.get_mV_temp(controller_MODBUS)
                self.DATA.result_list_SG600_main_temp[1]=temp_mV
        elif self.DATA.text_lcd_SG600_main_temp[1] == "C":
                temp_C = Controller_Client_MODBUS_Seneca.Controller_MODBUS.get_C_temp(controller_MODBUS)
                self.DATA.result_list_SG600_main_temp[1]=temp_C
        else:
                print("Error: something went wrong in the selection of the measuring unit in SG600 temp!")       
                exit(1)

if __name__ == "__main__":
    controllerTCP = Controller_Client_TCP_Laumas.Controller_TCP()
    controllerMODBUS = Controller_Client_MODBUS_Seneca.Controller_MODBUS()
    logger = LOGGER(nome_CSV="test", controller_TCP=controllerTCP, controller_MODBUS=controllerMODBUS, starting_status=True)

            
            
