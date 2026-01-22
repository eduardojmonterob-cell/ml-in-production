#1. pick up the model
    #1.1. if config file exists, load the trained model
    #1.2. if condig file does not exist, train model to get it
#2.make predictions

import pickle as pk
from pathlib import Path
from model import build_model


class ModelService:

    def __init__(self):
        self.model = None

    def load_model(self, model_name = 'rf_v1'):
        model_path = Path(f'models/{model_name}.pkl')

        if not model_path.exists():
            build_model()

        self.model = pk.load(open(model_path, 'rb'))


    def predict(self, input_parameters):
        return self.model.predict([input_parameters])


