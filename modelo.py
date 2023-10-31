import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Carregando o arquivo CSV do Demon Slayer em um DataFrame
demon_slayer_data = pd.read_csv('character.csv')

# Selecionando as colunas relevantes
features = ['Age', 'Abilities', 'Breathing Style']
target = 'Race'  # Nome da coluna para prever se o personagem é Humano ou Demônio

# Extraindo os recursos (features) e os rótulos (labels)
x = demon_slayer_data[features]
y = demon_slayer_data[target]

# Mapeando a coluna "Race" para valores binários (Humano: 0, Demônio: 1)
y = y.map({'Human': 0, 'Demon': 1})

# Treinando um classificador de árvore de decisão
clf = DecisionTreeClassifier()
clf = clf.fit(x, y)

# Salvando o modelo treinado em um arquivo
with open('demon_slayer_model.pkl', 'wb') as model_file:
    pickle.dump(clf, model_file)

print("Modelo treinado e salvo com sucesso!")
