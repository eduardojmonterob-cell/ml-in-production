"""
Este módulo proporciona funcionalidad para la gestión de un modelo de
Machine Learning.

Contiene la clase ModelService, que se encarga de cargar y utilizar un
modelo de ML previamente entrenado. La clase ofrece métodos para cargar
un modelo desde disco, construirlo si no existe y realizar predicciones
utilizando el modelo cargado.
"""

from pathlib import Path
import pickle as pk
from typing import Any, Iterable
    
from loguru import logger

from config.config import settings
from model.pipeline.model import build_model


class ModelService:
    """
    Servicio encargado de la carga y ejecución de modelos de Machine Learning.

    Esta clase centraliza la lógica de gestión del ciclo de vida del modelo,
    incluyendo su construcción, carga en memoria y ejecución de inferencias.

    Attributes
    ----------
    model : Any
        Instancia del modelo de Machine Learning cargado en memoria.
        Debe implementar el método `predict`.
    """

    def __init__(self) -> None:
        """Inicializa el servicio sin un modelo cargado en memoria."""
        self.model: Any | None = None

    def load_model(self, model_name: str) -> None:
        """Carga un modelo desde disco, construyéndolo si no existe."""
        model_path = Path(settings.model_path) / model_name

        logger.info(
            "Verificando la existencia del archivo del modelo en %s",
            model_path,
        )

        if not model_path.exists():
            logger.warning(
                "El modelo no fue encontrado en %s. Construyendo el modelo.",
                model_path,
            )
            build_model()

        logger.info("Cargando el modelo desde %s", model_path)

        with model_path.open("rb") as file:
            self.model = pk.load(file)

    def predict(self, input_parameters: Iterable[Any]) -> Any:
        """Realiza una predicción utilizando el modelo previamente cargado."""
        if self.model is None:
            raise RuntimeError(
                "El modelo no está cargado. Ejecute `load_model` antes de predecir."
            )

        logger.info("Realizando predicción")
        return self.model.predict([input_parameters])
    
    