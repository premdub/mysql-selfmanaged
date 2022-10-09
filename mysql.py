#!sudo apt-get install python3-dev default-libmysqlclient-devsudo apt-get install python3-dev default-libmysqlclient-dev
#pip install pymysql sqlalchemy
# pip install -u python-dotenv or
#pip install python-dotenv
from sqlalchemy import create_engine
import pandas as pd
import pymysql
import MySQLdb
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("PATH"))

MYSQL_HOSTNAME = os.getenv('MYSQL_HOSTNAME')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE =('brain_size_df')

connect_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_DATABASE}/{MYSQL_DATABASE}'
connect_string

db = create_engine(connect_string)




brain_size_df = pd.read_csv('https://raw.githubusercontent.com/premdub/descriptives_scipy/main/data/brain_size.csv')
brain_size_df


brain_size_df.to_sql('brain_size_table', con=db, if_exists="replace")


