# Importação das bibliotecas necessárias
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Definição da semente aleatória para a reprodutibilidade dos resultados
SEED = 20

# Definição da URL onde o arquivo CSV está localizado
uri = "https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv"

# Leitura dos dados do arquivo CSV e armazenamento em um DataFrame
dados = pd.read_csv(uri)

# Dicionário para renomear as colunas do DataFrame
mapa = {
    "home": "Principal",
    "how_it_works": "Como Funciona",
    "contact": "Contato",
    "bought": "Comprou"
}

# Renomeia as colunas do DataFrame usando o dicionário definido acima
dados = dados.rename(columns=mapa)

# Separação das colunas que serão usadas como entrada (x) e saída (y)
x = dados[["Principal", "Como Funciona", "Contato"]]
y = dados["Comprou"]

# Separação dos dados em conjunto de treino e conjunto de teste
treino_x, teste_x, treino_y, teste_y = train_test_split(
    x, y, random_state=SEED, test_size=0.25, stratify=y)

# Impressão do número de elementos nos conjuntos de treino e teste
print(
    f"treinaremos com {len(treino_x)}/100 elementos e testaremos com {len(teste_x)} elementos")

# Criação do modelo de classificação utilizando o algoritmo LinearSVC
modelo = LinearSVC()

# Treinamento do modelo utilizando o conjunto de treino
modelo.fit(treino_x, treino_y)

# Realização das previsões utilizando o conjunto de teste
previsoes = modelo.predict(teste_x)

# Cálculo da acurácia do modelo utilizando o conjunto de teste
acuracia = accuracy_score(teste_y, previsoes)

# Impressão da acurácia do modelo
print(f"O acerto foi de: {acuracia:.2%}")

# repare que o resultado será sempre o mesmo agora.
