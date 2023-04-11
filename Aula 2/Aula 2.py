'''
Análise de Dados com Python
Desafio: Você trabalha em uma empresa do varejo e tem milhares de clientes diferentes.

Com o objetivo de aumentar o faturamento e o lucro da sua empresa, a diretoria deseja
identificar quem é o cliente ideal para seus produtos, baseado no histórico de compras dos clientes.

Para isso, ela fez um trabalho de classificação dos clientes com uma nota de 1 a 100. E agora,
como analista de dados, a partir dessa nota, você deve descobrir qual o perfil de cliente ideal da empresa.
'''

import pandas as pd
import plotly.express as px # lib para trabalhar com gráficos

df_clientes = pd.read_csv("clientes.csv", encoding = "latin", sep=";") # Importa a base de dados

#Deleta a coluna 8 que está nos atrapalhando
df_clientes = df_clientes.drop("Unnamed: 8", axis=1) # axis 1 = coluna e axis 0 = linha

# corrige as informações que estão sendo reconhecidas de forma errada ... 'coerce' trata os casos
# de erros deletando-os
df_clientes["Salário Anual (R$)"] = pd.to_numeric(df_clientes["Salário Anual (R$)"], errors="coerce")

df_clientes = df_clientes.dropna() # Deleta as linhas que tem informações faltando

#Começando minhas análises no DF em forma de tabela:
print(df_clientes) #mostra um resumo do DF
print()
print(df_clientes.describe()) #Análise inicial
print()
print(df_clientes.info())  #mostra informações úteis sobre o DF

# Para trabalhar com gráfico, a sequencia é sempre construir o gráfico e depois mostrá-lo... Então:
# Construir o gráfico:
#grafico = px.histogram(df_clientes, x="Origem" , y="Nota (1-100)", histfunc="avg", text_auto="True")

# Mostrar o gráfico:
# grafico.show()
# Analise completa:

for coluna in df_clientes.columns:
    grafico = px.histogram(df_clientes, x=coluna , y="Nota (1-100)", histfunc="avg", text_auto="True")
    grafico.show()

'''
Veredito:
# Perfil ideal de cliente
# Acima de 15 anos (não tem muita diferença entra as faixas etárias depois disso)
# Faixa salarial não parece fazer tanta diferença
# Áreas de trabalho: 'Entretenimento' e 'Artista' (evitar 'Construção')
# Tem entre 10 e 15 anos de experiência
# Com familías não tão grandes (até no máximo 7 pessoas)
'''