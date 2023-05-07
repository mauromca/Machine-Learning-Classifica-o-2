## Machine-Learning-Classificão-2

### Processos do código:

* Importação das bibliotecas necessárias.
* Definição da semente aleatória para a reprodutibilidade dos resultados.
* Definição da URL onde o arquivo CSV está localizado.
* Leitura dos dados do arquivo CSV e armazenamento em um DataFrame.
* Dicionário para renomear as colunas do DataFrame.
* Renomeia as colunas do DataFrame usando o dicionário definido acima.
* Separação das colunas que serão usadas como entrada (x) e saída (y).
* Separação dos dados em conjunto de treino e conjunto de teste.
* Impressão do número de elementos nos conjuntos de treino e teste.
* Criação do modelo de classificação utilizando o algoritmo LinearSVC.
* Treinamento do modelo utilizando o conjunto de treino.
* Realização das previsões utilizando o conjunto de teste.
* Cálculo da acurácia do modelo utilizando o conjunto de teste.
* Impressão da acurácia do modelo.

### Resumo:

O código tem como objetivo criar um modelo de classificação capaz de prever se um usuário irá comprar ou não um produto baseado em suas interações com um site. Para isso, ele utiliza o **algoritmo LinearSVC** (*Support Vector Machine linear*) para treinar um modelo com base em um conjunto de dados de treinamento e, em seguida, avalia a precisão desse modelo em um conjunto de teste.

O processo começa importando as bibliotecas necessárias, que incluem **pandas** para trabalhar com dados, LinearSVC do pacote **scikit-learn** para criar o modelo de classificação, **accuracy_score** também do pacote scikit-learn para avaliar a precisão do modelo e **train_test_split** do pacote scikit-learn para dividir os dados em conjuntos de treinamento e teste.

Em seguida, a **semente aleatória** é definida para garantir que os resultados possam ser reproduzidos e a **URL** onde o **arquivo CSV** com os dados está localizado é definida. Os dados são então lidos a partir do arquivo CSV e armazenados em um **DataFrame**.

Para melhorar a legibilidade do DataFrame, as colunas são renomeadas usando um dicionário e o DataFrame é atualizado com as novas colunas. As colunas de entrada e saída são então separadas em variáveis distintas.

Os dados são divididos em conjuntos de treinamento e teste usando a função train_test_split. A proporção de dados no conjunto de teste é definida como **25%** e a **estratificação** é aplicada para garantir que a proporção de exemplos positivos e negativos seja a mesma em ambos os conjuntos.

O número de elementos nos conjuntos de treinamento e teste é impresso. O modelo LinearSVC é criado e treinado usando o conjunto de treinamento. Em seguida, o modelo é usado para fazer previsões com o conjunto de teste. A acurácia do modelo é calculada e impressa para avaliar sua eficácia em prever se um usuário irá comprar um produto ou não com base em suas interações com o site.
