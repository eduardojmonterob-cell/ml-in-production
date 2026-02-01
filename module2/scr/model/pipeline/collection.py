
import pandas as pd
from loguru import logger
from sqlalchemy import select

from config.config import engine, settings
from db.db_model import RentApartments


def load_data_from_db() -> pd.DataFrame:
    """
    Extraemos la tabla completa de RentApartments desde la base de datos.

    Returns:
    -------
        pd.DataFrame: Dataframe que contiene todos los registros de la tabla RentApartments.
    """
    logger.info('extracting the table from database')
    query = select(RentApartments)
    return pd.read_sql(
        query, 
        engine,
        )

   