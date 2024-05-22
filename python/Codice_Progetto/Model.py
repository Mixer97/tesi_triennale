# Questo Model ha il compito di tenere dentro di se i dati della sessione e i dati necessari al controller.
# NON DEVE COMUNICARE DIRETTAMENTE CON LA VIEW

import pandas as pd 
import Controller_Client_TCP
from time import process_time
import time
import csv

class Logger:
    # Costruttore di default
    def __init__(self, nome_CSV = None, status_EXEC = None):
        self.nome_CSV = nome_CSV
        self.status_EXEC = status_EXEC
    
    # Getter nome CSV corrente
    def CSV_name_getter(self):
        return f"{self.nome_CSV}"
    
    # Setter nome CSV
    def CSV_name_setter(self, nuovo_nome_CSV):
        self.nome_CSV = nuovo_nome_CSV
    
    # Getter path completo di dive salvare il CSV
    def CSV_path_getter(self):
        self.path_CSV = f'Codice_Progetto\\CSV\\{self.nome_CSV}.csv'
        return f"{self.path_CSV}"
    
    # Getter status esecuzione logger
    def status_EXEC_getter(self):
        return f"{self.status_EXEC}"            # Check per vedere se torna
    
    # Setter status esecuzione logger
    def status_EXEC_setter(self, status=False):
        self.status_EXEC = status
    
    # Esecuzione del logger 
    def execute_logger(self):
        
        path_CSV = self.CSV_path_getter()
        
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
        start_timer = time.time()  
            
        while True:
            if self.status_EXEC:
                # Processing dei dati
                stop_timer = time.time()
                timer = stop_timer - start_timer
                
                # Lettura dei registri mV
                result_list = Controller_Client_TCP.WORKING.read_holding_registers_mV()   
                
                # Scrittura di una riga
                with open(path_CSV, mode="a", newline="") as csv_doc:
                    writer = csv.writer(csv_doc)
                    list_to_write = [timer, result_list[0], result_list[1], result_list[2], result_list[3], "mV"]
                    writer.writerow(list_to_write)
                    print(list_to_write) 
                    
if __name__ == "__main__":
    logger = Logger("test", True)
    logger.execute_logger()
    
    