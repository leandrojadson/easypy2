
import pandas as pd
from datetime import datetime, timedelta


from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

def __init__(self): 
    self.token = "c54T8efvkaOeeWdNpCLrzouJQjWWHnMDEuCsTPikh9FZJJVRbdTJ3-8uomcUdNLSrq256dBxOXhC8FouE98OBg=="
    self.org = "Organization_N"
    self.bucket = "Data"
    self._client = InfluxDBClient(url="http://leandro-freitas.de:8086", token=self.token, org=self.org)

    
def dataframe_to_influx():
    _now = datetime.utcnow()

    _data_frame = pd.DataFrame(data=[["cfafaeek", 11.0],["uuidtest1", 5.0]],
                                        index=[_now + timedelta(hours=2), _now + timedelta(hours=2)],
                                        columns=["uuid", "value"])
    print(_data_frame.head())
     
    #_data_frame.select("value").map(_.getInt(0)).collect.toSeq 
    
    query = 'from(bucket: "Data") |> range(start: -1h)'
    tables = client.query_api().query(query, org=self.org)
    for table in tables:
        for record in table.records:
            print(record)

if __name__ == '__main__':
    dataframe_to_influx()
