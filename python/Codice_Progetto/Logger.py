# importing the module 
import pandas as pd 
import Controller_Client_TCP_Laumas as Controller_Client_TCP_Laumas
import Controller_Client_MODBUS_Seneca
import time
from time import sleep
import csv

class DATA:
    startStop_logger=False
    text_lcd=["mV","mV","mV","mV"]  # Viene aggiornata dalla Main_View in automatico
    result_list_1_4=[0,0,0,0]
    result_list_SG600_main_temp=[0,0]
    text_lcd_SG600_main_temp=["mV","mV"]  # Viene aggiornato dalla Main View in automatico [[DA IMPLEMENTARE]] 
    loop_status=True

def logger(nome_CSV):
    
    path_CSV = 'C:\\Code_GIT\\tesi_triennale_Git\\python\\Codice_Progetto\\CSV\\' + str(nome_CSV) + ".csv"
    
    # Creazione liste per dataframe
    list_time = []
    list_cella1 = []
    list_cella2 = []  
    list_cella3 = [] 
    list_cella4 = [] 
    list_SG600_main = []
    list_SG600_temp = []
    list_unit_t = []
    list_unit_1 = []
    list_unit_2 = []
    list_unit_3 = []
    list_unit_4 = []
    list_SG600_main_unit = []
    list_SG600_temp_unit = []
    
    
    
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
            'unit_4':list_unit_4,
            'SG600_main':list_SG600_main,
            'unit_main':list_SG600_main_unit,
            'SG600_temp':list_SG600_temp,
            'unit_temp':list_SG600_temp_unit,} 
    
    df = pd.DataFrame(my_df) 
    
    # saving the DataFrame as a CSV file 
    df.to_csv(path_CSV, index=False)  
            
        # timer start
    timer = 0
    start_timer = time.time()  
        
    while DATA.loop_status:
        sleep(0.10)   # tmer per gestire la frequenza di campionamento del logger
        if DATA.startStop_logger:
            # Processing dei dati
            stop_timer = time.time()
            timer = stop_timer - start_timer

            # Aggiornamento logger con unità di misura necessarie
            update_CH1()
            update_CH2()
            update_CH3()
            update_CH4()
            update_SG600_main()
            update_SG600_temp()
            
            # Scrittura di una riga
            with open(path_CSV, mode="a", newline="") as csv_doc:
                writer = csv.writer(csv_doc)
                list_to_write = [timer,
                                "s",
                                DATA.result_list_1_4[0],
                                DATA.text_lcd[0],
                                DATA.result_list_1_4[1],
                                DATA.text_lcd[1],
                                DATA.result_list_1_4[2],
                                DATA.text_lcd[2],
                                DATA.result_list_1_4[3],
                                DATA.text_lcd[3],
                                DATA.result_list_SG600_main_temp[0],
                                DATA.text_lcd_SG600_main_temp[0],
                                DATA.result_list_SG600_main_temp[1],
                                DATA.text_lcd_SG600_main_temp[1],
                                ]
                
                writer.writerow(list_to_write)  # Scrittura di una riga del CSV
                print(list_to_write)    # Print di testing

def update_CH1():
    if DATA.text_lcd[0] == "mV":
            list_mV = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_mv()
            DATA.result_list_1_4[0]=list_mV[0]
    elif DATA.text_lcd[0] == "Kg":
            list_Kg = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_Kg()
            DATA.result_list_1_4[0]=list_Kg[0]
    elif DATA.text_lcd[0] == "N":
            list_N = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_N()
            DATA.result_list_1_4[0]=list_N[0]
    elif DATA.text_lcd[0] == "Nm":
            list_Nm = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_Nm()
            DATA.result_list_1_4[0]=list_Nm[0]
    else:
            print("Error: something went wrong in the selection of the measuring unit in CH1!")       
            exit(1)
            
def update_CH2():
    if DATA.text_lcd[1] == "mV":
            list_mV = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_mv()
            DATA.result_list_1_4[1]=list_mV[1]
    elif DATA.text_lcd[1] == "Kg":
            list_Kg = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_Kg()
            DATA.result_list_1_4[1]=list_Kg[1]
    elif DATA.text_lcd[1] == "N":
            list_N = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_N()
            DATA.result_list_1_4[1]=list_N[1]
    elif DATA.text_lcd[1] == "Nm":
            list_Nm = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_Nm()
            DATA.result_list_1_4[1]=list_Nm[1]
    else:
            print("Error: something went wrong in the selection of the measuring unit in CH2!")       
            exit(1)
            
def update_CH3():
    if DATA.text_lcd[2] == "mV":
            list_mV = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_mv()
            DATA.result_list_1_4[2]=list_mV[2]
    elif DATA.text_lcd[2] == "Kg":
            list_Kg = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_Kg()
            DATA.result_list_1_4[2]=list_Kg[2]
    elif DATA.text_lcd[2] == "N":
            list_N = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_N()
            DATA.result_list_1_4[2]=list_N[2]
    elif DATA.text_lcd[2] == "Nm":
            list_Nm = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_Nm()
            DATA.result_list_1_4[2]=list_Nm[2]
    else:
            print("Error: something went wrong in the selection of the measuring unit in CH3!")       
            exit(1)
            
def update_CH4():
    if DATA.text_lcd[3] == "mV":
            list_mV = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_mv()
            DATA.result_list_1_4[3]=list_mV[3]
    elif DATA.text_lcd[3] == "Kg":
            list_Kg = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_Kg()
            DATA.result_list_1_4[3]=list_Kg[3]
    elif DATA.text_lcd[3] == "N":
            list_N = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_N()
            DATA.result_list_1_4[3]=list_N[3]
    elif DATA.text_lcd[3] == "Nm":
            list_Nm = Controller_Client_TCP_Laumas.DATA_INTERACTIONS.get_Nm()
            DATA.result_list_1_4[3]=list_Nm[3]
    else:
            print("Error: something went wrong in the selection of the measuring unit in CH4!")       
            exit(1)
            
def update_SG600_main():
    if DATA.text_lcd_SG600_main_temp[0] == "mV":
            main_mV = Controller_Client_MODBUS_Seneca.DATA_INTERACTIONS.get_mV_main()
            DATA.result_list_SG600_main_temp[0]=main_mV
#   elif DATA.text_lcd_SG600_main_temp[0] == "Nm":
#           main_Nm = Controller_Client_MODBUS_Seneca.DATA_INTERACTIONS.get_Nm()
#           DATA.result_list_SG600_main_temp[0]=main_Nm
    else:
            print("Error: something went wrong in the selection of the measuring unit in SG600 main!")       
            exit(1)
            
def update_SG600_temp():
    if DATA.text_lcd_SG600_main_temp[1] == "mV":
            temp_mV = Controller_Client_MODBUS_Seneca.DATA_INTERACTIONS.get_mV_temp()
            DATA.result_list_SG600_main_temp[1]=temp_mV
#   elif DATA.text_lcd_SG600_main_temp[1] == "C":
#           temp_C = Controller_Client_MODBUS_Seneca.DATA_INTERACTIONS.get_Nm()
#           DATA.result_list_SG600_main_temp[1]=temp_C
    else:
            print("Error: something went wrong in the selection of the measuring unit in SG600 temp!")       
            exit(1)


if __name__ == "__main__":
    DATA.startStop_logger = True
    logger(nome_CSV="test")
        
        
