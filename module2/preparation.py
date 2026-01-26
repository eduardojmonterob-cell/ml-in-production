
import re
import pandas as pd
from collection import load_data
from loguru import logger

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

    columns = ['balcony', 'parking', 'furnished', 'garage', 'storage']
    logger.info(f'Encoding columns {columns} ...')

    return pd.get_dummies(data, 
                          columns=columns,
                          drop_first=True)


def parse_garden_col(data):
    
    logger.info(f'Parsing column garden ...')
    data = data.apply(lambda x: int(re.findall(r'\d+', x)[0]) if x != 'Not present' else 0)

    return data
