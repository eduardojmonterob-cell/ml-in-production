"""
Carga de datos de apartamentos en alquiler desde la base de datos.

Este módulo contiene utilidades para extraer información de la tabla
`RentApartments` utilizando SQLAlchemy y cargarla en un `pandas.DataFrame`
para su posterior análisis o procesamiento.

La conexión a la base de datos se obtiene desde la configuración de la
aplicación y se utiliza el motor (`engine`) definido globalmente.
El módulo también incorpora logging para facilitar el seguimiento del
proceso de extracción de datos.
"""

import pandas as pd
from loguru import logger
from sqlalchemy import select

from config import engine
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

