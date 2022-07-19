import pandas as pd
import os.path

file = '/home/python/app/data.csv'
file_exists = os.path.exists(file)

#test path
print(file_exists)

#test csv
df = pd.read_csv(file, sep=';')
print(df['Value']) 

#test move file

