"""
Preparación y transformación de datos de apartamentos en alquiler.

Este módulo contiene funciones auxiliares para preparar el conjunto de
datos de apartamentos en alquiler antes de su uso en análisis o modelos
de machine learning. Incluye la carga de datos desde la base de datos,
la codificación de variables categóricas y la transformación de columnas
específicas a formatos numéricos.

Las funciones aquí definidas operan principalmente sobre objetos
`pandas.DataFrame` y forman parte del pipeline de preprocesamiento
de datos de la aplicación.
"""

import re

import pandas as pd
from loguru import logger

from model.pipeline.collection import load_data_from_db


def prepare_data() -> pd.DataFrame:
    """
    Prepara el conjunto de datos de apartamentos en alquiler.

    Inicia el pipeline de procesamiento cargando los datos desde la base
    de datos, codificando las variables categóricas relevantes y
    transformando la columna `garden` a un formato numérico.

    Returns:
        pd.DataFrame: DataFrame con los datos procesados y listos para su
        uso en análisis o modelos de machine learning.
    """
        
    logger.info('starting up processing pipeline')
    dataframe = load_data_from_db()
    data_encoded = _enconde_cat_cols(dataframe) 

    data_encoded['garden'] = _parse_garden_col(data_encoded['garden'])
    return data_encoded


def _enconde_cat_cols(data: pd.DataFrame) -> pd.DataFrame:
    """
    Codifica columnas categóricas del conjunto de datos.

    Transforma las columnas categóricas especificadas en variables
    numéricas mediante codificación one-hot, eliminando la primera
    categoría para evitar multicolinealidad.

    Args:
        data (pd.DataFrame): DataFrame de entrada con columnas
            categóricas a codificar.

    Returns:
        pd.DataFrame: DataFrame con las columnas categóricas codificadas.
    """
    columns = ['balcony', 'parking', 'furnished', 'garage', 'storage']
    logger.info(f'Encoding caregorical columns {columns}')

    return pd.get_dummies(
        data, 
        columns=columns,
        drop_first=True)


def _parse_garden_col(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza la columna `garden` a un formato numérico.

    Convierte los valores de la columna `garden` en enteros, extrayendo
    cantidades numéricas cuando están presentes y asignando el valor
    cero cuando el jardín no está disponible.

    Args:
        data (pd.DataFrame): Serie o columna del DataFrame que representa
            la información del jardín.

    Returns:
        pd.DataFrame: Columna transformada con valores numéricos.
    """

    logger.info(f'Parsing column garden')
    dataframe = dataframe.apply(lambda x: int(re.findall(r'\d+', x)[0]) if x != 'Not present' else 0)

    return dataframe
