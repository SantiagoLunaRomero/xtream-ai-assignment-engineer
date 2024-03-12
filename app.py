from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load('saved_models/RandomForest.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener datos de entrada del cuerpo de la solicitud POST
        data = request.get_json()
        # Convertir los datos en un DataFrame de pandas
        features = pd.DataFrame(data, index=[0])
        # Hacer predicción
        prediction = model.predict(features)
        # Devolver la predicción como respuesta JSON
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

    