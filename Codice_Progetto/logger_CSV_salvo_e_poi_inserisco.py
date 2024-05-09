# importing the module 
import pandas as pd 
import client_Sinc_TCP
import project_PySide6_ui
from time import process_time, sleep
import time

startStop = project_PySide6_ui.startStop

# Creazione liste
list_time = []
list_cella1 = []
list_cella2 = []  
list_cella3 = [] 
list_cella4 = [] 
list_unit = []


def logger():
    
    timer = 0
    n = 0
    start_timer = time.time()  # timer start
    
    while timer <= 1.000000000000:
        # Processing dei dati
        stop_timer = time.time()
        timer = stop_timer - start_timer
        n = n + 1
        
        # result_list = client_Sinc_TCP.WORKING.read_holding_registers_mV() # RENDERE PIU VELOCE

        list_time.append(timer)
        # list_cella1.append(result_list[0])
        # list_cella2.append(result_list[1])
        # list_cella3.append(result_list[2])
        # list_cella4.append(result_list[3])
        list_unit.append('mV')
        
        # print(list_cella3)
        print(timer)
        print(n)

if __name__ == "__main__":
    logger()