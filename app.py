from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

# Carregar o modelo treinado
model = pickle.load(open("model_beer_style.pkl", "rb"))

# Carregar o conjunto de dados de cervejas
df = pd.read_csv('beer_reviews.csv')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Coletar dados do formulário HTML
        features = [
            float(request.form['review_overall']),
            float(request.form['review_aroma']),
            float(request.form['review_appearance']),
            float(request.form['review_palate']),
            float(request.form['review_taste']),
            float(request.form['beer_abv'])
        ]

        # Realizar a previsão
        pred = model.predict([features])
        predicted_style = pred[0]

        return render_template("index.html", prediction_text=f"Estilo previsto: {predicted_style}")

    except Exception as e:
        return render_template("index.html", prediction_text="Erro: Certifique-se de preencher todos os campos corretamente.")

@app.route("/api", methods=["POST"])
def api_predict():
    try:
        data = request.get_json()

        # Coletar dados do JSON
        review_overall = float(data['review_overall'])
        review_aroma = float(data['review_aroma'])
        review_appearance = float(data['review_appearance'])
        review_palate = float(data['review_palate'])
        review_taste = float(data['review_taste'])
        beer_abv = float(data['beer_abv'])

        # Realizar a previsão
        features = [review_overall, review_aroma, review_appearance, review_palate, review_taste, beer_abv]
        pred = model.predict([features])
        predicted_style = pred[0]

        return jsonify({"predicted_style": predicted_style})

    except Exception as e:
        return jsonify({"error": "Erro: Certifique-se de enviar os dados corretamente."})

if __name__ == "__main__":
    app.run(debug=True)
