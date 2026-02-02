"""
Proporciona un servicio para la gestión de modelos de Machine Learning.

Este módulo contiene la clase `ModelService`, que encapsula la lógica para
cargar, construir y utilizar modelos de ML para realizar predicciones.
Simplifica la interacción con el modelo, manejando su ciclo de vida desde
la carga desde el disco hasta la ejecución de inferencias.
"""

from pathlib import Path
import pickle as pk
from sklearn.ensemble import RandomForestRegressor
    
from loguru import logger

from config import model_settings
from model.pipeline.model import build_model

    
class ModelService:
    """
    Gestiona el ciclo de vida y las predicciones de un modelo de ML.

    Esta clase centraliza la lógica de gestión del ciclo de vida del modelo,
    incluyendo su construcción, carga en memoria y ejecución de inferencias.

    Attributes
    ----------
    model : RandomForestRegressor | None
        Instancia del modelo de Machine Learning cargado en memoria.
        Es `None` si no se ha cargado ningún modelo.
    """

    def __init__(self) -> None:
        """Inicializa una instancia de ModelService."""
        self.model: RandomForestRegressor | None = None

    def load_model(self, model_name: str) -> None:
        """
        Carga un modelo de machine learning desde un archivo.

        Si el archivo del modelo no existe en la ruta especificada, se invoca
        a la función `build_model` para entrenar y guardar un nuevo modelo.

        Parameters
        ----------
        model_name : str
            Nombre del archivo del modelo a cargar (ej. 'model.pkl').
        """
        model_path = Path(model_settings.model_path) / model_name

        logger.info(
            'Verificando la existencia del archivo del modelo en %s',
            model_path,
        )

        if not model_path.exists():
            logger.warning(
                'El modelo no fue encontrado en %s. Construyendo el modelo.',
                model_path,
            )
            build_model()

        logger.info('Cargando el modelo desde %s', model_path)

        with model_path.open("rb") as file:
            self.model = pk.load(file)

    def predict(self, input_parameters: list) -> list:
        """
        Realiza una predicción utilizando el modelo cargado.

        Parameters
        ----------
        input_parameters : Iterable[Any]
            Un iterable con los datos de entrada para la predicción.

        Returns
        -------
        list
            El resultado de la predicción del modelo.

        Raises
        ------
        RuntimeError
            Si se intenta predecir sin haber cargado un modelo previamente.
        """
        if self.model is None:
            raise RuntimeError(
                'El modelo no está cargado. Ejecute `load_model` antes de predecir.'
            )

        logger.info('Realizando predicción')
        return self.model.predict([input_parameters])
