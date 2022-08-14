from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import os.path
import pandas as pd

from influxdb import DataFrameClient

from datetime import datetime

file = '/home/python/app/data.csv'
file_exists = os.path.exists(file)

#test csv
df = pd.read_csv(file, sep=';')

# You can generate an API token from the "API Tokens Tab" in the UI
token = "c54T8efvkaOeeWdNpCLrzouJQjWWHnMDEuCsTPikh9FZJJVRbdTJ3-8uomcUdNLSrq256dBxOXhC8FouE98OBg=="
org = "Organization_N"
bucket = "Data"




client = InfluxDBClient(url="http://leandro-freitas.de:8086", token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)


file = '/home/python/app/data.csv'
file_exists = os.path.exists(file)

#test path


#test csv
df = pd.read_csv(file, sep=';')
             
#df['Date']= pd.to_datetime(df['Date'])
df['Date'].astype(str)


df= df.set_index('Date')

# Preparing Dataframe:  

#print(df)

# DataFrame must have the timestamp column as an index for the client. 
              
df2= df['VIX Low']
#client = InfluxDBClient(host="http://leandro-freitas.de", port="8086", user="admin", password="Pwadmin123")

#df2.to_timestamp('%Y-%m-%d %I-%p')
#df2.values.tolist()
for row in df2.index:
    pp=df2.loc[[row]]
    pp.to_string(index=False, header=False)
    #row =  row.astype(int).apply(str)
    print (row)
    point = Point("mem") \
    .tag("host", "host1") \
    .field("used_percent", pp) \
    .time(row)
    write_api.write(bucket, org, point)

#time_precision='ms')
  
#print(df2)
#df2.index=pd.to_datetime(df2.index)

#xx = DataFrameClient._convert_dataframe_to_json(df,'test2')

#print(xx)
#list_num = ['mem','host1']   

#sequence = df2
#print (sequence)
#write_api.write(bucket, org, sequence)


client.close()

