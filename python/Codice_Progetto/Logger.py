# importing the module 
import pandas as pd 
import Controller_Client_TCP as Controller_Client_TCP
import time
from time import sleep
import csv

class DATA:
    startStop_logger=False
    text_lcd=["mV","mV","mV","mV"]  # Viene aggiornata dalla View in automatico
    result_list=[0,0,0,0]

def logger(nome_CSV):
    
    path_CSV = 'C:\\Code_GIT\\tesi_triennale_Git\\python\\Codice_Progetto\\CSV\\' + str(nome_CSV) + ".csv"
    
    # Creazione liste per dataframe
    list_time = []
    list_cella1 = []
    list_cella2 = []  
    list_cella3 = [] 
    list_cella4 = [] 
    list_unit_t = []
    list_unit_1 = []
    list_unit_2 = []
    list_unit_3 = []
    list_unit_4 = []
    
    
    
     # creating the DataFrame 
    my_df = {'Time': list_time,
            'unit_Time':list_unit_t,  
            'Cella_1': list_cella1,
            'unit_1':list_unit_1, 
            'Cella_2': list_cella2,
            'unit_2':list_unit_2, 
            'Cella_3': list_cella3,
            'unit_3':list_unit_3, 
            'Cella_4': list_cella4,  
            'unit_4':list_unit_4, } 
    
    df = pd.DataFrame(my_df) 
    
    # saving the DataFrame as a CSV file 
    df.to_csv(path_CSV, index=False)  
            
        # timer start
    timer = 0
    start_timer = time.time()  
        
    while True:
        sleep(0.10)   # Aggiunto per testing
        if DATA.startStop_logger:
            # Processing dei dati
            stop_timer = time.time()
            timer = stop_timer - start_timer

            # Aggiornamento logger con unità di misura necessarie
            update_CH1()
            update_CH2()
            update_CH3()
            update_CH4()
            
            # Scrittura di una riga
            with open(path_CSV, mode="a", newline="") as csv_doc:
                writer = csv.writer(csv_doc)
                list_to_write = [timer, "s", DATA.result_list[0], DATA.text_lcd[0], DATA.result_list[1], DATA.text_lcd[1], DATA.result_list[2], DATA.text_lcd[2], DATA.result_list[3], DATA.text_lcd[3]]
                writer.writerow(list_to_write)
                print(list_to_write) 

def update_CH1():
    if DATA.text_lcd[0] == "mV":
            list_mV = Controller_Client_TCP.DATA_INTERACTIONS.get_mv()
            DATA.result_list[0]=list_mV[0]
    elif DATA.text_lcd[0] == "Kg":
            list_Kg = Controller_Client_TCP.DATA_INTERACTIONS.get_Kg()
            DATA.result_list[0]=list_Kg[0]
    elif DATA.text_lcd[0] == "N":
            list_N = Controller_Client_TCP.DATA_INTERACTIONS.get_N()
            DATA.result_list[0]=list_N[0]
    elif DATA.text_lcd[0] == "Nm":
            list_Nm = Controller_Client_TCP.DATA_INTERACTIONS.get_Nm()
            DATA.result_list[0]=list_Nm[0]
    else:
            print("Error: something went wrong in the selection of the measuring unit in CH1!")       
            exit(1)
            
def update_CH2():
    if DATA.text_lcd[1] == "mV":
            list_mV = Controller_Client_TCP.DATA_INTERACTIONS.get_mv()
            DATA.result_list[1]=list_mV[1]
    elif DATA.text_lcd[1] == "Kg":
            list_Kg = Controller_Client_TCP.DATA_INTERACTIONS.get_Kg()
            DATA.result_list[1]=list_Kg[1]
    elif DATA.text_lcd[1] == "N":
            list_N = Controller_Client_TCP.DATA_INTERACTIONS.get_N()
            DATA.result_list[1]=list_N[1]
    elif DATA.text_lcd[1] == "Nm":
            list_Nm = Controller_Client_TCP.DATA_INTERACTIONS.get_Nm()
            DATA.result_list[1]=list_Nm[1]
    else:
            print("Error: something went wrong in the selection of the measuring unit in CH2!")       
            exit(1)
            
def update_CH3():
    if DATA.text_lcd[2] == "mV":
            list_mV = Controller_Client_TCP.DATA_INTERACTIONS.get_mv()
            DATA.result_list[2]=list_mV[2]
    elif DATA.text_lcd[2] == "Kg":
            list_Kg = Controller_Client_TCP.DATA_INTERACTIONS.get_Kg()
            DATA.result_list[2]=list_Kg[2]
    elif DATA.text_lcd[2] == "N":
            list_N = Controller_Client_TCP.DATA_INTERACTIONS.get_N()
            DATA.result_list[2]=list_N[2]
    elif DATA.text_lcd[2] == "Nm":
            list_Nm = Controller_Client_TCP.DATA_INTERACTIONS.get_Nm()
            DATA.result_list[2]=list_Nm[2]
    else:
            print("Error: something went wrong in the selection of the measuring unit in CH3!")       
            exit(1)
            
def update_CH4():
    if DATA.text_lcd[3] == "mV":
            list_mV = Controller_Client_TCP.DATA_INTERACTIONS.get_mv()
            DATA.result_list[3]=list_mV[3]
    elif DATA.text_lcd[3] == "Kg":
            list_Kg = Controller_Client_TCP.DATA_INTERACTIONS.get_Kg()
            DATA.result_list[3]=list_Kg[3]
    elif DATA.text_lcd[3] == "N":
            list_N = Controller_Client_TCP.DATA_INTERACTIONS.get_N()
            DATA.result_list[3]=list_N[3]
    elif DATA.text_lcd[3] == "Nm":
            list_Nm = Controller_Client_TCP.DATA_INTERACTIONS.get_Nm()
            DATA.result_list[3]=list_Nm[3]
    else:
            print("Error: something went wrong in the selection of the measuring unit in CH4!")       
            exit(1)

if __name__ == "__main__":
    DATA.startStop_logger = True
    logger(nome_CSV="test")
        
        
