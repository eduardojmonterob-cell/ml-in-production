from flask import Blueprint, request, abort
from pydantic import ValidationError

from services.model_inference import ModelInferenceService
from schema.apartment import Apartment
from services import model_inference_service

bp = Blueprint('prediction', __name__, url_prefix='/pred')

@bp.get('/')
def get_prediction():

    # get and check input parameters
    try:
        apartment_features = Apartment(**request.args)
    except ValidationError:
        abort(400, description='Bad input parameters')

    # feed input parameters to the loaded ml model to get a predition
    prediction = model_inference_service.predict(
        list(apartment_features.model_dump().values()),
        )

    # return a prediction value
    return {'prediction': prediction}


@bp.post('/')
def get_prediction_post():

    # get and check input parameters
    try:
        apartment_features = Apartment(**request.json)
    except ValidationError:
        abort(400, description='Bad input parameters')

    # feed input parameters to the loaded ml model to get a predition
    prediction = model_inference_service.predict(
        list(apartment_features.model_dump().values()),
        )


    # return a prediction value
    return {'prediction': prediction}