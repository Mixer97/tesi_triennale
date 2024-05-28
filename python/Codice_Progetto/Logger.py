# importing the module 
import pandas as pd 
import Controller_Client_TCP as Controller_Client_TCP
import View_QT as View_QT
from time import process_time
import time
import csv


def logger(nome_CSV):
    
    path_CSV = 'C:\\Code_GIT\\tesi_triennale_Git\\python\\Codice_Progetto\\CSV\\' + str(nome_CSV) + ".csv"
    
    # Creazione liste per dataframe
    list_time = []
    list_cella1 = []
    list_cella2 = []  
    list_cella3 = [] 
    list_cella4 = [] 
    list_unit = [] 

     # creating the DataFrame 
    my_df = {'Time [s]': list_time,  
            'Cella_1': list_cella1,
            'Cella_2': list_cella2,
            'Cella_3': list_cella3,
            'Cella_4': list_cella4,  
            'unit': list_unit} 
    df = pd.DataFrame(my_df) 
    
    # saving the DataFrame as a CSV file 
    df.to_csv(path_CSV, index=False)  
            
        # timer start
    timer = 0
    n = 0
    start_timer = time.time()  
        
    while True:
        if View_QT.startStop_logger:
            # Processing dei dati
            stop_timer = time.time()
            timer = stop_timer - start_timer
            
            # Lettura dei registri mV
            result_list = Controller_Client_TCP.DATA_INTERACTIONS.get_mv()
            
            # Scrittura di una riga
            with open(path_CSV, mode="a", newline="") as csv_doc:
                writer = csv.writer(csv_doc)
                list_to_write = [timer, result_list[0], result_list[1], result_list[2], result_list[3], "mV"]
                writer.writerow(list_to_write)
                print(list_to_write) 

if __name__ == "__main__":
    View_QT.startStop_logger = True
    logger(nome_CSV="test")
        
        
