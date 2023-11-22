import requests

url = 'http://localhost:5000/api'
data = {
    "review_overall": 4,
    "review_aroma": 4.5,
    "review_appearance": 4,
    "review_palate": 4,
    "review_taste": 4.5,
    "beer_abv": 7.5
}

r = requests.post(url, json=data)

result = r.json()
if "predicted_style" in result:
    print(f"Estilo previsto: {result['predicted_style']}")
else:
    print("Erro na resposta da API.")
