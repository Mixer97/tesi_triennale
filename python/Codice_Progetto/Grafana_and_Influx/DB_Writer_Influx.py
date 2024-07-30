from __future__ import annotations
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from time import sleep
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA



class DB_Writer:
    
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA):
        self.banco_di_taratura = banco_di_taratura
        
        # Dati registrati di Euramet
        self.list_main_temp = self.banco_di_taratura.logger.DATA.result_list_SG600_main_temp
        self.list_units_main_temp = self.banco_di_taratura.logger.DATA.text_lcd_SG600_main_temp
        self.list_units_laumas = self.banco_di_taratura.logger.DATA.text_lcd
        self.list_channels_laumas = self.banco_di_taratura.logger.DATA.result_list_1_4
        
        # Inizializzazione del writer
        self.token = "pdD6zV4_tp9NjqJOaUE4Y7QQOOncsTWX1b2cCyWwnbGYBAvleLIkQxouNllRaYCe8_d5rDwrZoZoMdHMQkEV8g=="
        self.org = "Database"
        self.url = "http://localhost:8086"
        self.bucket="Euramet Data"
        print(self.token)
        
        client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
        
        # oggetto per scrivere nel DB
        self.write_api = client.write_api(write_options=SYNCHRONOUS)

    

    