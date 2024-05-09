# importing the module 
import pandas as pd 
import client_Sinc_TCP
import project_PySide6_ui
from time import process_time
import time

startStop = project_PySide6_ui.startStop

def logger():
    
    # Creazione liste per dataframe
    list_time = []
    list_cella1 = []
    list_cella2 = []  
    list_cella3 = [] 
    list_cella4 = [] 
    list_unit = [] 

    # creating the DataFrame 
    my_df = {'Time': list_time,  
            'Cella_1': list_cella1,
            'Cella_2': list_cella2,
            'Cella_3': list_cella3,
            'Cella_4': list_cella4,  
            'unit': list_unit} 
    df = pd.DataFrame(my_df) 
    
    # displaying the DataFrame 
    print('DataFrame:\n', df) 
    
    # saving the DataFrame as a CSV file 
    gfg_csv_data = df.to_csv('Codice_Progetto\\CSV\\testing_log.csv', index=False) 
    print('\nCSV String:\n', gfg_csv_data) 
    
    
    timer = 0
    n = 0
    start_timer = time.time()  # timer start
    
    while timer <= 1.00000000000:
        # Processing dei dati
        

        stop_timer = time.time()
        timer = stop_timer - start_timer
        n = n + 1  
        
        result_list = client_Sinc_TCP.WORKING.read_holding_registers_mV() 

        # creating the DataFrame 
        my_df = [[timer,
                 result_list[0],
                 result_list[1],
                 result_list[2],
                 result_list[3],
                 'mV']] 
        df = pd.DataFrame(my_df)  
        
        df.to_csv('Codice_Progetto\\CSV\\testing_log.csv', header=False, mode='a', index=False)       

        print(timer)
        print(n)
    


if __name__ == "__main__":
    startStop = True
    logger()