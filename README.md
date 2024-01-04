# Classificador de Cerveja usando IA

Este projeto consiste em um aplicativo de classificação de cervejas que utiliza um modelo de Aprendizado de Máquina. Aqui estão as informações necessárias para treinar o modelo e executar o aplicativo.

## Tecnologias Utilizadas

### Treinamento do Modelo (modelo.py)
- **Linguagem de Programação:** Python
- **Bibliotecas:**
  - *pandas:* Manipulação e análise de dados.
  - *scikit-learn (sklearn):* Implementação do algoritmo Decision Tree Classifier.
  - *pickle:* Para salvar e carregar o modelo treinado.

Para treinar o modelo, execute o arquivo `modelo.py`. Este script utiliza o arquivo `beer_reviews.csv` como tabela de treinamento.

### Aplicativo Web (app.py)
- **Linguagem de Programação:** Python
- **Framework Web:** Flask
- **Frontend:** HTML, CSS (pode ser estendido conforme necessário)
- **Backend:** Flask
- **Comunicação Frontend-Backend:** Flask
- **Integração com Modelo:** Utiliza o modelo treinado pelo `modelo.py`.

Para iniciar o aplicativo, execute o arquivo `app.py`. O aplicativo oferece uma interface web para inserção de informações sobre a cerveja e utiliza o modelo treinado para realizar a classificação.

## Execução do Projeto

1. Execute `modelo.py` para treinar o modelo.
2. Execute `app.py` para iniciar o aplicativo web.
3. Acesse o aplicativo via navegador.

### Nota:
- Certifique-se de ter as bibliotecas necessárias instaladas usando `pip install -r requirements.txt`.


## Colaboração

O projeto foi desenvolvido em colaboração com [André Luiz de Lima](https://github.com/andredevsec/) e é uma separação do repositório [FlaskLudimilo](https://github.com/andredevsec/flaskludimilo).