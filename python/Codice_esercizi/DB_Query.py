from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS


if __name__ == "__main__":

    token = "pdD6zV4_tp9NjqJOaUE4Y7QQOOncsTWX1b2cCyWwnbGYBAvleLIkQxouNllRaYCe8_d5rDwrZoZoMdHMQkEV8g=="
    org = "Database"
    url = "http://localhost:8086"
    bucket="BUCKET"
    print(token)

    client = InfluxDBClient(
        url=url,
        token=token,
        org=org
    )

    # Query script
    query_api = client.query_api()
    query = f'from(bucket:"{bucket}")\
    |> range(start: -10m)\
    |> filter(fn:(r) => r._measurement == "Euramet")\
    |> filter(fn:(r) => r.rampa == "Precarico")'

    result = query_api.query(org=org, query=query)
    results = []
    for table in result:
        for record in table.records:
            results.append((record.get_field(), record.get_value()))

    i=0
    for element in results:
        print(f'{element} --> {i}')
        i+=1