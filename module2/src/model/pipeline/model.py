
"""
Módulo de entrenamiento y persistencia de un modelo de regresión para predicción de alquileres.

Este módulo implementa el flujo completo de machine learning para entrenar un modelo
`RandomForestRegressor`, incluyendo:
- Preparación de los datos.
- Separación en conjuntos de entrenamiento y prueba.
- Búsqueda de hiperparámetros mediante `GridSearchCV`.
- Evaluación del modelo usando la métrica R².
- Persistencia del modelo entrenado en disco.

La configuración de rutas y nombres del modelo se obtiene desde el módulo `config`,
y la preparación de los datos se delega al pipeline de preprocesamiento.

Dependencias principales:
- scikit-learn
- loguru
- pickle

Uso típico:
    >>> build_model()
"""
import pandas as pd
import pickle as pk
import warnings

from loguru import logger
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestRegressor

from config import model_settings
from model.pipeline.preparation import prepare_data

warnings.filterwarnings('ignore')

def build_model() -> None:
    """
    Ejecuta el pipeline completo de entrenamiento, evaluación y guardado del modelo.

    La función realiza de forma secuencial los siguientes pasos:
    1. Obtiene y prepara el dataset mediante el pipeline de preprocesamiento.
    2. Separa las variables independientes (X) y la variable objetivo (y).
    3. Divide los datos en conjuntos de entrenamiento y prueba.
    4. Entrena un modelo de Random Forest optimizando hiperparámetros con GridSearchCV.
    5. Evalúa el modelo utilizando la métrica R² sobre el conjunto de test.
    6. Guarda el modelo entrenado en la ruta configurada.

    Returns
    -------
    None
        La función no retorna ningún valor. El modelo entrenado se persiste en disco.
    """

    df = prepare_data()
    feature_names = [
        'area', 
        'constraction_year', 
        'bedrooms', 
        'garden', 
        'balcony_yes', 
        'parking_yes', 
        'furnished_yes', 
        'garage_yes', 
        'storage_yes'
    ]
    X, y = _get_x_y(
        df,
        col_x= feature_names)
    X_train, X_test, y_train, y_test = _split_train_test(
        X,
        y,
    )
    model = _train_model(
        X_train,
        y_train,
    )
    score = _evaluate_model(
        model,
        X_test,
        y_test,
    )
    logger.info(f'Model R2 score: {score}')
    _save_model(model, path= f'{model_settings.model_path}/{model_settings.model_name}')

def _get_x_y(
        data: pd.DataFrame,
        col_x: list[str],
        col_y: str = 'rent'
    ) -> tuple[pd.DataFrame, pd.Series]:
    """
    Separa el dataset en variables explicativas (X) y variable objetivo (y).

    Parameters
    ----------
    data : pd.DataFrame
        Dataset completo con features y variable objetivo.
    col_x : list[str]
        Lista de nombres de columnas que se utilizarán como variables independientes.
    col_y : str, default='rent'
        Nombre de la columna objetivo.

    Returns
    -------
    tuple[pd.DataFrame, pd.Series]
        - X: DataFrame con las variables independientes.
        - y: Serie con la variable objetivo.
    """
        
    logger.info('Identifying X and y ...')
    return data[col_x], data[col_y] 
            
def _split_train_test(
        features: pd.DataFrame,
        target: pd.Series, 
    ) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Divide las variables X e y en conjuntos de entrenamiento y prueba.

    Parameters
    ----------
    features (pd.DataFrame): Variables independientes.
    target (pd.Series): Variable objetivo.

    Returns
    -------
    tuple: Training and testing sets for features and target.
    """
    logger.info('Splitting X and y ...')
    X_train, X_test, y_train, y_test = train_test_split(
        features, 
        target,
        test_size=0.2,
        random_state=42
    )
    return X_train, X_test, y_train, y_test


def _train_model(
        X_train: pd.DataFrame,
        y_train: pd.Series,
    )-> RandomForestRegressor:
    """
    Entrena un modelo RandomForestRegressor optimizando hiperparámetros.

    Se utiliza GridSearchCV para seleccionar la mejor combinación de
    hiperparámetros en función de la métrica R².

    Parameters
    ----------
    X_train : pd.DataFrame
        Variables independientes del conjunto de entrenamiento.
    y_train : pd.Series
        Variable objetivo del conjunto de entrenamiento.

    Returns
    -------
    RandomForestRegressor
        Modelo entrenado con los mejores hiperparámetros encontrados.
    """
    logger.info('Training the model ...')
    grid_space = {
        'n_estimators': [100, 200, 300], 
        'max_depth': [3, 6, 9, 12],
    }
    
    grid = GridSearchCV(
        RandomForestRegressor(), 
        param_grid=grid_space, 
        cv=5, 
        scoring = 'r2',
    )

    model_grid = grid.fit(
        X_train,
        y_train,
        )
    model = model_grid.best_estimator_

    return model

def _evaluate_model(
        model: RandomForestRegressor, 
        X_test:pd.DataFrame,
        y_test: pd.Series,
    )-> float:
    """
    Evalúa el modelo entrenado sobre el conjunto de prueba.

    Parameters
    ----------
    model : RandomForestRegressor
        Modelo previamente entrenado.
    X_test : pd.DataFrame
        Variables independientes del conjunto de prueba.
    y_test : pd.Series
        Variable objetivo del conjunto de prueba.

    Returns
    -------
    float
        Score R² obtenido sobre el conjunto de test.
    """
    logger.info('Evaluating and tunning the model ...')
    return model.score(
        X_test,
        y_test,
        )

def _save_model(model: RandomForestRegressor, path: str)-> None:
    """
    Persiste el modelo entrenado en disco utilizando pickle.

    Parameters
    ----------
    model : object
        Modelo entrenado a serializar.
    path : str
        Ruta completa donde se guardará el modelo serializado.

    Returns
    -------
    None
        La función no retorna ningún valor.
    """
    logger.info(f'saving the model to a directory: {path}')
    with open(path, 'wb') as model_file:
        pk.dump(model, model_file)
