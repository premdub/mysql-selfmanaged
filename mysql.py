#!sudo apt-get install python3-dev default-libmysqlclient-devsudo apt-get install python3-dev default-libmysqlclient-dev
#pip install pymysql sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import pymysql
MYSQL_HOSTNAME = '35.193.75.235'
MYSQL_USER = 'pdubey'
MYSQL_PASSWORD = 'prem4321'
MYSQL_DATABASE ='real_df'
connect_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
connect_string
db = create_engine(connect_string)
db

#db = pd.read_sql(query,con=db)
#db
brain_size_df = pd.read_csv('https://raw.githubusercontent.com/premdub/descriptives_scipy/main/data/brain_size.csv')
brain_size_df
brain_size_df.to_sql('brain_size_table', con=db, if_exists="replace")


