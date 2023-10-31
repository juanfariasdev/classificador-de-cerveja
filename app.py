import numpy as np
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Carregar o modelo treinado
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Coletar dados do formulário HTML
        age = int(request.form['Age'])
        abilities = request.form['Abilities']
        breathing_style = request.form['Breathing Style']

        # Realizar a previsão
        pred = model.predict([[age, abilities, breathing_style]])
        prediction_text = "Hashira" if pred[0] == 1 else "Outro"

        return render_template("index.html", prediction_text=prediction_text)

    except Exception as e:
        return render_template("index.html", prediction_text="Erro: Certifique-se de preencher todos os campos corretamente.")

if __name__ == "__main":
    app.run(debug=True)
