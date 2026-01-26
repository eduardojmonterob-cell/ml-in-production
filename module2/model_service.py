#1. pick up the model
    #1.1. if config file exists, load the trained model
    #1.2. if condig file does not exist, train model to get it
#2.make predictions

import pickle as pk
from pathlib import Path
from model import build_model

from config import settings

class ModelService:

    def __init__(self):
        self.model = None

    def load_model(self, model_name):
        model_path = Path(f'{settings.model_path}/{model_name}')


        if not model_path.exists():
            build_model()

        self.model = pk.load(open(f'{settings.model_path}/{settings.model_name}', 'rb'))


    def predict(self, input_parameters):
        return self.model.predict([input_parameters])


