# importing the module 
import pandas as pd 
import client_Sinc_TCP
import QT_Creator_dell_App_4_ui
from time import process_time
import time


def logger():
    
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
    df.to_csv('Codice_Progetto\\CSV\\testing_log.csv', index=False)  
    
    # timer start
    timer = 0
    n = 0
    start_timer = time.time()  
    
    while True:
        if QT_Creator_dell_App_4_ui.startStop_logger:
            # Processing dei dati
            stop_timer = time.time()
            timer = stop_timer - start_timer
            
            # lettura dei registri mV
            result_list = client_Sinc_TCP.WORKING.read_holding_registers_mV()   

            # creating the DataFrame 
            my_df = [[timer,
                    result_list[0],
                    result_list[1],
                    result_list[2],
                    result_list[3],
                    'mV']] 
            df = pd.DataFrame(my_df)  
            
            # Append al file CSV 
            df.to_csv('Codice_Progetto\\CSV\\testing_log.csv', header=False, mode='a', index=False) 
            n = n + 1 
            print(n)   


if __name__ == "__main__":
    QT_Creator_dell_App_4_ui.startStop_logger
    logger()