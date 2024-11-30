import sqlite3
import pandas as pd
from setup import load_config
import os
import utils.preprocess as preprocess

# run in src dir
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# load configuration 
config = load_config()

db_path = config['database']['db_path']
conn= sqlite3.connect(db_path)
# Find table name 
tablename_query = "SELECT name FROM sqlite_master WHERE type='table';"
tablename= pd.read_sql_query(tablename_query, conn)

# Get data from database
df_query = f"SELECT * FROM {tablename.iloc[0,0]};"
df= pd.read_sql_query(df_query, conn)