import mysql.connector
from mysql.connector import Error

import os.path
import pandas as pd
from datetime import datetime

file = '/home/python/app/data.csv'
file_exists = os.path.exists(file)

#test csv
df = pd.read_csv(file, sep=';')


import mysql.connector as mysql

# enter your server IP address/domain name
HOST = "http://leandro-freitas.de:3306" # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "energy"
# this is the user you create
USER = "user"
# user password
PASSWORD = "pwdb2"
# connect to MySQL server
db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to:", db_connection.get_server_info())
# enter your code here!