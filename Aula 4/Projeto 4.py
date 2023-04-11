''' Projeto Ciência de Dados - Previsão de Preços
Nosso desafio é conseguir prever o preço de barcos que vamos vender baseado nas características do barco,
como: ano, tamanho, tipo de barco, se é novo ou usado, qual material usado, etc.

- Passo 1: Entendimento do Desafio
- Passo 2: Entendimento da Área/Empresa
- Passo 3: Extração/Obtenção de Dados
- Passo 4: Ajuste de Dados (Tratamento/Limpeza)
- Passo 5: Análise Exploratória
- Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
- Passo 7: Interpretação de Resultados
'''

import pandas as pd # importa o Pandas
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split # importa a train_test_split da sklearn
from sklearn import metrics

tabela = pd.read_csv("barcos_ref.csv") #Importa o banco de dados dos 'Barcos'
print(tabela)

# Agora vamos ver a CORRELAÇÃO da coluna PREÇO com as demais colunas:
teste = tabela.corr()[["Preco"]]
teste = teste.sort_values("Preco", ascending=False) # organiza de forma decrescente
# print(teste)

# Para facilitar a visualização, transformaremos em gráfico:

# teste = teste.drop('Preco', axis=0) #Exclui a correlação Preço x Preço
sns.heatmap(teste, annot=True, cmap="Blues")
plt.show()

# Preparação das massas de dados:

y = tabela["Preco"] # Y é o que queremos chegar
x = tabela.drop("Preco", axis=1) # Tirando o 'Preço', aqui é todo o restante que daremos para a IA aprender a calcular

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1) # parametrizando a IA, onde:
'''Massa de treino:
    x_treino: Dados que a IA usará para treinar
    y_treino: Resultados esperados que a IA deverá chegar durante o treino
    
    Massa de teste:
    x_teste: Dados que a IA usará para TESTAR (imputará estes dados e verá os resultados)
    y_teste: Resultados esperados que a IA deverá chegar durante o TESTE'''

#Criação das IAs:

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# cria as inteligencias aritificiais
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# treina as inteligencias artificiais com as massas de dados
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)


# criar as previsoes
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

# comparar os modelos
print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))

'''Após verificar a saída destes 2 prints:
    Nota-se que o modelo de 'Árvore de decisão' se saiu MUITO melhor com quase o dobro de precisão'''

#Vamos ver isso em um gráfico:

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste #resultados 'reais' dos preços dos barcos
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvoredecisao #Preços dos barcos pelo modelo 'Árvore de Decisão'
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressaolinear #Preços dos barcos pelo modelo 'Regressão Linear'

sns.lineplot(data=tabela_auxiliar)
plt.show()

sns.lineplot(data=tabela_auxiliar[["y_teste", "Previsoes ArvoreDecisao"]])
plt.show()

sns.lineplot(data=tabela_auxiliar[["y_teste", "Previsoes Regressao Linear"]])
plt.show()

# Com o modelo escolhido e treinado ('Árvore de Decisão'), chegou a hora de passarmos novos barcos
# para ele precificar:

nova_tabela = pd.read_csv("novos_barcos.csv") # importa a tabela com os novos modelos de barcos
print(nova_tabela) # Mostra a tabela com as informações dos novos barcos

previsao = modelo_arvoredecisao.predict(nova_tabela) # insere estas informações para o modelo de predição

print(previsao.round(2)) #  Mostra o valor de cada barco, segundo o nosso modelo