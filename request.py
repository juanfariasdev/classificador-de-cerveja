import requests

url = 'http://localhost:5000/api'
data = {
    "Age": 16,
    "Abilities": "Water Breathing, Hinokami Kagura",
    "FightingStyle": "Water Breathing"
}

r = requests.post(url, json=data)

result = r.json()
if "is_hashira" in result:
    if result["is_hashira"]:
        print("Este personagem é um Hashira!")
    else:
        print("Este personagem não é um Hashira!")
else:
    print("Erro na resposta da API.")
