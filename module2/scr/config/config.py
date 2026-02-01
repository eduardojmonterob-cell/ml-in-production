"""
Este módulo centraliza la configuración de la aplicación.

Define la clase Settings, encargada de cargar variables de entorno
utilizando Pydantic, así como la inicialización del sistema de logging
y la conexión a la base de datos.
"""

from loguru import logger
from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine


class Settings(BaseSettings):
    """
    Configuración de la aplicación basada en variables de entorno.

    Las variables se cargan desde el archivo `.env` y se validan
    automáticamente mediante Pydantic.

    Attributes
    ----------
    model_path : DirectoryPath
        Ruta al directorio que contiene los archivos de configuración
        y serialización del modelo.
    model_name : str
        Nombre del archivo del modelo a utilizar.
    log_level : str
        Nivel de logging de la aplicación (por ejemplo, INFO, DEBUG).
    db_conn_str : str
        Cadena de conexión a la base de datos.
    rent_apartment_table_name : str
        Nombre de la tabla utilizada para almacenar los datos de alquiler.
    """

    model_config = SettingsConfigDict(
        env_file="config/.env",
        env_file_encoding="utf-8",
    )

    model_path: DirectoryPath
    model_name: str
    log_level: str
    db_conn_str: str
    rent_apartment_table_name: str


def configure_logging(log_level: str) -> None:
    """Configura el sistema de logging utilizando Loguru.
    
    Arg:
        log_level (str): Nivel de logging deseado.

    Returns:
        None
    """
    logger.remove()  # Elimina los manejadores por defecto
    logger.add(
        "logs/app.log",
        rotation="1 day",
        retention="2 days",
        compression="zip",
        level=log_level,
    )

# Inicialización de la configuración y el logging
settings = Settings()
configure_logging(log_level= settings.log_level)

# Creamos el db engine 
engine = create_engine(settings.db_conn_str)

