import sqlite3
import os
import sys
import yaml

def load_config():
    config_path =  os.path.join(os.path.dirname(__file__),'config.yaml')
    with open(config_path,"r") as file :
        return yaml.safe_load(file)