
from model.model_service import ModelService
from config.config import settings
from loguru import logger

def main():
    ml_svc = ModelService()
    ml_svc.load_model(settings.model_name)
    predict = ml_svc.predict([50, 2000, 2, 10, 1, 0, 1, 0, 1])
    logger.warning(f'Prediction: {predict}')


if __name__ == "__main__":
    main()