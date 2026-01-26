import pandas as pd
from config import settings
from loguru import logger

def load_data(path=settings.data_file_name): # data_file_name    
    # Load data from a CSV file into a DataFrame
    
    logger.info(f'Loading data from {path} ...')
    df = pd.read_csv(path)
    return df
