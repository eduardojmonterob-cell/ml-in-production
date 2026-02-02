"""
Este modulo contiene los parámetros cargados desde variables de entorno
necesarios para localizar e identificar el proceso de logging.
"""
from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

class LoggerSettings(BaseSettings):
    """
    Logger confuguration settings for the application.

    Attributes:
        mode_config (SettingConfigDict): Model config, loaded from .env file.
        log_level (str): Logging level for the application

    """

    model_config = SettingsConfigDict(
        env_file="config/.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    log_level: str




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
        #compression="zip",
        level=log_level,
    )


configure_logging(log_level= LoggerSettings().log_level)

