import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Carregando o arquivo beer_reviews.csv em um DataFrame
beer_data = pd.read_csv('beer_reviews.csv')

# Selecionando as colunas relevantes
features = ['review_overall', 'review_aroma', 'review_appearance', 'review_palate', 'review_taste', 'beer_abv']
target = 'beer_style'  # Alterado para prever o estilo de cerveja

# Extraindo os recursos (features) e os rótulos (labels)
x = beer_data[features]
y = beer_data[target]

# Realizando o split da base para teste
from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# Treinando um classificador de árvore de decisão
clf = DecisionTreeClassifier()
clf = clf.fit(x_treino, y_treino)

# Realizando previsões
preditos = clf.predict(x_teste)
print("Preditos:", preditos)
print("Real    :", y_teste)

# Salvando o modelo treinado em um arquivo
pickle.dump(clf, open('model_beer_style.pkl', 'wb'))
model = pickle.load(open('model_beer_style.pkl', 'rb'))
