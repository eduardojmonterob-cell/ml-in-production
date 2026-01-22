
import re
import pandas as pd
from collection import load_data

def prepare_data():
    pass
    # To prepare the data we need:

    #1. Load the dataset
    data = load_data()
    #2. enconde columns like balcony, parking, furnished, garage, storage
    data_encoded = enconde_cat_cols(data) 
    #3. parse garden column
    data_encoded['garden'] = parse_garden_col(data_encoded['garden'])

    return data_encoded

def enconde_cat_cols(data):

    return pd.get_dummies(data, 
                          columns=['balcony', 'parking', 'furnished', 'garage', 'storage'],
                          drop_first=True)


def parse_garden_col(data):
    
    data = data.apply(lambda x: int(re.findall(r'\d+', x)[0]) if x != 'Not present' else 0)

    return data


#df = prepare_data()
#print(df['garden'])