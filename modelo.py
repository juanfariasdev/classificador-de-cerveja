import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

class Modelo:
    def __init__(self):
        # Dados de exemplo
        data = {
            'Character': ['Goku', 'Krillin', '139', '5,000,000,000', 'Saiyan Saga', 'Baby Saga', 'Dragon Ball Z', 'Dragon Ball GT', 'Goku', 'Bulma'],
            'Power_Level': [4, 3, 139, 5000000000, 5, 5, 74, 17, 10, 1.5],
            'Saga_or_Movie': ['Dragon Ball', 'Dragon Ball', 'Other', 'Other', 'Saiyan Saga', 'Baby Saga', 'Other', 'Other', 'Emperor Pilaf Saga', 'Emperor Pilaf Saga'],
            'Dragon_Ball_Series': ['Dragon Ball', 'Dragon Ball', 'Other', 'Other', 'Dragon Ball Z', 'Dragon Ball Z', 'Dragon Ball Z', 'Dragon Ball GT', 'Dragon Ball', 'Dragon Ball']
        }

        # Criando um DataFrame
        self.df = pd.DataFrame(data)

        # Selecionando as colunas relevantes
        self.features = ['Power_Level']
        self.target = 'Is_Super_Saiyan'

        # Definindo se um personagem é Super Saiyan com base no Power_Level
        self.df['Is_Super_Saiyan'] = self.df['Power_Level'] > 8000

        # Extraindo os recursos (features) e os rótulos (labels)
        self.X = self.df[self.features]
        self.y = self.df[self.target]

        # Treinando um classificador de árvore de decisão
        self.clf = None  # Inicialmente, o modelo não está treinado

    def train_model(self):
        self.clf = DecisionTreeClassifier()
        self.clf.fit(self.X, self.y)
        # Salvando o modelo treinado em um arquivo
        with open('dbz_model.pkl', 'wb') as model_file:
            pickle.dump(self.clf, model_file)

    def create_character(self, character_name, power_level, saga_or_movie, db_series):
        if self.clf is None:
            self.train_model()

        # Gera uma previsão para o novo personagem
        power_level = float(power_level)
        is_super_saiyan = self.clf.predict([[power_level]])[0]

        response = f"Nome do Personagem: {character_name}<br>"
        response += f"Saga ou Filme: {saga_or_movie}<br>"
        response += f"Série do Dragon Ball: {db_series}<br>"
        response += f"Nível de Poder: {power_level}<br>"
        response += "Este personagem é um Deus Super Saiyajin." if is_super_saiyan else "Este personagem não é um Deus Super Saiyajin."

        return response

# Exemplo de uso
model = Modelo()
character_info = model.create_character('Vegeta', 9000, 'Saiyan Saga', 'Dragon Ball Z')
print(character_info)
