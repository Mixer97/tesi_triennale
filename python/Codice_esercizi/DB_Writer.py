from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from time import sleep
import random



if __name__ == "__main__":
    
    token = "pdD6zV4_tp9NjqJOaUE4Y7QQOOncsTWX1b2cCyWwnbGYBAvleLIkQxouNllRaYCe8_d5rDwrZoZoMdHMQkEV8g=="
    org = "Database"
    url = "http://localhost:8086"
    bucket="BUCKET"
    print(token)
    
    client = InfluxDBClient(url=url, token=token, org=org)
    
    # oggetto per scrivere nel DB
    write_api = client.write_api(write_options=SYNCHRONOUS)

    # creo un punto e lo scrivo nel bucket del DB
    while True:
        p = Point("Euramet").tag("rampa", "Precarico").field("main", 2*random.random()).field("temp", 50*random.random())
        write_api.write(bucket=bucket, org=org, record=p)
        sleep(0.1)
    

    