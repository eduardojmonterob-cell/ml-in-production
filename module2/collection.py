import pandas as pd
from config import settings
from loguru import logger

from config import engine
from db_model import RentApartments
from sqlalchemy import select



def load_data(path): # data_file_name    
    # Load data from a CSV file into a DataFrame
    
    logger.info(f'Loading data from {path} ...')
    df = pd.read_csv(path)
    return df

def load_data_from_db():
    logger.info('extracting the table from database ...')
    query = select(RentApartments)
    return pd.read_sql(query, engine)   