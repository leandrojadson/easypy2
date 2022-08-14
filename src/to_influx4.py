from datetime import datetime, timedelta

import pandas as pd
import reactivex as rx
from reactivex import operators as ops

from influxdb_client import InfluxDBClient, Point, WriteOptions


import os.path
import pandas as pd
from datetime import datetime

file = '/home/python/app/data.csv'
file_exists = os.path.exists(file)

#test csv
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
df = pd.read_csv(file, sep=';')
        

#df['Date']= pd.to_datetime(df['Date'])
df['Date'].astype(str)
df['Date']=pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d %H:%M:%S.%f")

df= df.set_index('Date')
df = df.rename(columns={'VIX Low': 'water_level'})
df2= df['water_level']
df2 = df2.rename_axis(None)
df2.columns =['water_level']

# Preparing Dataframe:  

# DataFrame must have the timestamp column as an index for the client. 
              

# You can generate an API token from the "API Tokens Tab" in the UI
token = "c54T8efvkaOeeWdNpCLrzouJQjWWHnMDEuCsTPikh9FZJJVRbdTJ3-8uomcUdNLSrq256dBxOXhC8FouE98OBg=="
org = "Organization_N"
bucket = "Data"





with InfluxDBClient(url="http://leandro-freitas.de:8086", token=token, org=org) as _client:

    with _client.write_api(write_options=WriteOptions(batch_size=500,
                                                      flush_interval=10_000,
                                                      jitter_interval=2_000,
                                                      retry_interval=5_000,
                                                      max_retries=5,
                                                      max_retry_delay=30_000,
                                                      exponential_base=2)) as _write_client:

 
        """
        Write Pandas DataFrame
        """
        _now = datetime.utcnow()
        _data_frame = df2
        _data_frame = pd.DataFrame(data=df2,
                                   index=df2.index,
                                   columns=["water_level"])

        #_data_frame = pd.DataFrame(data=[["coyote_creek", 1.0], ["coyote_creek", 2.0]],
         #                          index=[_now, _now + timedelta(hours=1)],
          #                         columns=["location", "water_level"])
        print(_data_frame)
        _write_client.write(bucket, org, record=_data_frame, data_frame_measurement_name='azul',
                            data_frame_tag_columns=['location'])