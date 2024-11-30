import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA

def clean_data(data,config):

    """
    General data cleaning Drop duplicates, missing_data,lowercase strings
    project specific datacleaning
    """
    clean_config= config['preprocess']['clean']
    
    if clean_config['drop_duplicates']:
        data = data.drop_duplicate()
    if clean_config['drop_na']:
        data = data.drop_na()
    data = data.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)
    # cleaning specific to project, drop unique identifier and take absolute value of checkoutdays
    data['checkout_day'] = data['checkout_day'].abs()
    df_cleaned= df_cleaned.drop(['booking_id'],axis=1)

    return data 

def feature_engineering(data,config):
    FE_config= config['preprocess']['FE']
    
    if FE_config['price_converter']:
     data = price_converter(data)

    return data





def price_converter(data):
    """
    Parse string of currency and convert it to amount in SGD
    """
    conversion_rates = {
    'usd': 1.34,  # Example: 1 USD = 1.37 SGD
    'sgd': 1.00,  # SGD remains the same
    }
    data['currency']= data['price'].str.extract(r'(\w+)\$')
    data['amount']= data['price'].str.extract(r'\$ (\d+(\.\d+)?)')[0].astype(float)
    data['amount_in_sgd'] = data.apply(lambda row: row['amount'] * conversion_rates.get(row['currency'].lower(), 1), axis=1).round(2)
    # drop irrelevant price column
    data= data.drop(['amount','price','currency'],axis=1 )
    
    return data

