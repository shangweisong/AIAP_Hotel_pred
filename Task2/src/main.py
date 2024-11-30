import sqlite3
import pandas as pd
from setup import load_config
import os

# run in src dir
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# load configuration 
config = load_config()

db_path = config['database']['db_path']
conn= sqlite3.connect(db_path)