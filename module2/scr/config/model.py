"""
Este modulo contiene los parámetros cargados desde variables de entorno
necesarios para localizar e identificar el modelo a utilizar.
"""

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict

class ModelSettings(BaseSettings):
    """
    Configuración del modelo.

    Carga los parámetros del modelo desde variables de entorno
    (archivo `config/.env`) utilizando Pydantic `BaseSettings`.

    Atributos
    ----------
    model_path : DirectoryPath
        Ruta al directorio donde se encuentra el modelo.
    model_name : str
        Nombre del modelo.
    """

    model_config = SettingsConfigDict(
        env_file="config/.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    model_path: DirectoryPath
    model_name: str

model_settings = ModelSettings()