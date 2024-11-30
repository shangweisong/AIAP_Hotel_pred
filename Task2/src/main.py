import sqlite3
import pandas as pd
from setup import load_config

# load configuration 
config = load_config()

db_path = config['database']['db_path']
conn= sqlite3.connect(db_path)