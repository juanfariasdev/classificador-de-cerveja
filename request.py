import requests

class DragonBallCharacterPredictor:
    def __init__(self, api_url):
        self.api_url = api_url

    def predict_character(self, data):
        try:
            r = requests.post(self.api_url, json=data)
            result = r.json()

            if "is_super_saiyan" in result:
                if result["is_super_saiyan"]:
                    return "Este personagem é um Deus Super Saiyajin!"
                else:
                    return "Este personagem não é um Deus Super Saiyajin!"
            else:
                return "Erro na resposta da API."
        except Exception as e:
            return f"Erro na solicitação à API: {str(e)}"

# Exemplo de uso
if __name__ == "__main__":
    api_url = 'http://localhost:5000/api'
    predictor = DragonBallCharacterPredictor(api_url)

    data = {
        "Power_Level": 9000
    }

    result = predictor.predict_character(data)
    print(result)
