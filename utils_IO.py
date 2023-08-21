import pandas as pd
from influxdb import InfluxDBClient


def get_data(query):
    # Connect to InfluxDB and fetch data
    client = InfluxDBClient(host='10.10.10.11')
    client.switch_database('ISS')
    
    results = client.query(query)
    client.close()

    return pd.DataFrame.from_records(results.get_points())