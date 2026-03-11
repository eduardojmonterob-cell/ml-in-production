
"""
Punto de entrada para la carga y ejecución de predicciones del modelo entrenado.

Este módulo actúa como script principal para:
- Inicializar el servicio de modelo (`ModelService`).
- Cargar un modelo previamente entrenado desde la ruta configurada.
- Ejecutar una predicción de ejemplo utilizando un conjunto fijo de features.
- Registrar el resultado de la predicción mediante logging.

Está pensado para validaciones rápidas, pruebas locales o ejecuciones manuales
del modelo entrenado, y no para entrenamiento.

Uso típico:
    >>> python main.py
"""

from loguru import logger

from model.model_service import ModelService
from config import model_settings

@logger.catch
def main()-> None:
    """
    Carga un modelo entrenado y ejecuta una predicción de ejemplo.

    La función inicializa el servicio de modelo, carga el modelo previamente
    entrenado desde la ruta configurada y realiza una predicción utilizando
    un conjunto fijo de features. El resultado de la predicción se registra
    mediante el sistema de logging.
    """
    logger.info('running the application...')
    ml_svc = ModelService()
    ml_svc.load_model(model_name=model_settings.model_name)

    feature_values = {
        'area': 50,
        'constraction_year': 2000,
        'bedrooms': 2,
        'garden': 10,
        'balcony_yes': 1,
        'parking_yes': 0,
        'furnished_yes': 1,
        'garage_yes': 0,
        'storage_yes': 1,
    }

    predict = ml_svc.predict(list(feature_values.values()))
    logger.warning(f'Prediction: {predict}')


if __name__ == "__main__":
    main()
