import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import logging
import joblib
import os

# Configuración básica del logging
logging.basicConfig(filename='pipeline.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def load_and_clean_data(file_path):
    """Carga y limpia el conjunto de datos."""
    try:
        diamonds_df = pd.read_csv(file_path)
        diamonds_df_cleaned = diamonds_df[(diamonds_df['price'] > 0) & (diamonds_df['x'] > 0) & (diamonds_df['y'] > 0) & (diamonds_df['z'] > 0)]
        diamonds_df_encoded = pd.get_dummies(diamonds_df_cleaned, columns=['cut', 'color', 'clarity'])
        logging.info("Data loaded and cleaned successfully.")
        return diamonds_df_encoded
    except Exception as e:
        logging.error(f"Error loading and cleaning data: {e}")
        raise e

def split_data(data):
    """Divide los datos en conjuntos de entrenamiento, validación y prueba."""
    X = data.drop('price', axis=1)
    y = data['price']
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=(20/90), random_state=42)
    return X_train, X_val, X_test, y_train, y_val, y_test

def train_models(X_train, y_train):
    """Entrena los modelos especificados y devuelve un diccionario con ellos."""
    try:
        models = {
            'Ridge': Ridge(alpha=1.0),
            'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42)
        }
        for name, model in models.items():
            model.fit(X_train, y_train)
            logging.info(f"{name} model trained successfully.")
        return models
    except Exception as e:
        logging.error(f"Error training models: {e}")
        raise e

def evaluate_models(models, X_val, y_val):
    """Evalúa los modelos y devuelve sus RMSE."""
    results = {}
    for name, model in models.items():
        y_pred = model.predict(X_val)
        rmse = np.sqrt(mean_squared_error(y_val, y_pred))
        results[name] = rmse
        logging.info(f"{name} model evaluated with RMSE: {rmse}")
    return results

def save_models(models):
    """Guarda los modelos entrenados."""
    if not os.path.exists('saved_models'):
        os.makedirs('saved_models')
    for name, model in models.items():
        joblib.dump(model, f'saved_models/{name}.joblib')
        logging.info(f"{name} model saved.")

def run_pipeline(file_path):
    """Función principal del pipeline."""
    try:
        data = load_and_clean_data(file_path)
        X_train, X_val, X_test, y_train, y_val, y_test = split_data(data)
        models = train_models(X_train, y_train)
        results = evaluate_models(models, X_val, y_val)
        save_models(models)
        logging.info("Pipeline executed successfully.")
        print(results)
    except Exception as e:
        logging.error(f"Error in pipeline execution: {e}")

# Ejecutar el pipeline
file_path = 'datasets/diamonds/diamonds.csv'
run_pipeline(file_path)