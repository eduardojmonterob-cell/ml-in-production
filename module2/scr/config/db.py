"""
Este modulo contiene los parámetros cargados desde variables de entorno
necesarios para localizar e identificar el proceso de logging.
"""
from sqlalchemy import create_engine 
from pydantic_settings import BaseSettings, SettingsConfigDict

class DbSettings(BaseSettings):
    """
    DB confuguration settings for the application.

    Attributes:
        mode_config (SettingConfigDict): Model config, loaded from .env file.
        log_level (str): Logging level for the application

    """

    model_config = SettingsConfigDict(
        env_file="config/.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    db_conn_str: str
    rent_apartment_table_name: str

db_settings = DbSettings()

engine = create_engine(db_settings.db_conn_str)