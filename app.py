import numpy as np
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Carregar o modelo treinado
model = pickle.load(open("dbz_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create_character", methods=["POST"])
def create_character():
    try:
        character = request.form['Character']
        saga_or_movie = request.form['Saga_or_Movie']
        dragon_ball_series = request.form['Dragon_Ball_Series']

        # Gerar um nível de poder aleatório para o novo personagem
        power_level = np.random.uniform(1, 5000000000)

        # Verificar se o nível de poder é maior que 8000
        is_super_saiyan = power_level > 8000

        response = f"Nome do Personagem: {character}<br>"
        response += f"Saga ou Filme: {saga_or_movie}<br>"
        response += f"Série do Dragon Ball: {dragon_ball_series}<br>"
        response += f"Nível de Poder: {power_level}<br>"
        response += "Este personagem é um Deus Super Saiyajin." if is_super_saiyan else "Este personagem não é um Deus Super Saiyajin."

        return render_template("index.html", creation_response=response)

    except Exception as e:
        return render_template("index.html", creation_response="Erro: Certifique-se de preencher todos os campos corretamente.")

if __name__ == "__main":
    app.run(debug=True)
