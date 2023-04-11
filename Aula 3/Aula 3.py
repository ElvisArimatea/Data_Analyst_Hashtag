'''
Automação Web e Busca de Informações com Python
Desafio: Trabalhamos em uma importadora e compramos e vendemos commodities:
    -> Soja, Milho, Trigo, Petróleo, etc.
Precisamos obter na internet, de forma automatizada, a cotação de todas as commodites e ver
se ela está abaixo do nosso preço ideal de compra. Se tiver, precisamos marcar como uma ação de
compra para a equipe de operações.

Para isso, vamos criar uma automação web utilizando Selenium
'''

from selenium import webdriver as wd # Importa 'webdriver' do selenium
import pandas as pd                  # Importa o Pandas

navegador = wd.Chrome()             # Cria uma instancia do Chrome para ser controlada

df_commodities = pd.read_excel("commodities.xlsx") #Importa nossa base de dados (incompleta)

print(df_commodities)
#df_commodities.info()

link = "https://www.noticiasagricolas.com.br/cotacoes/milho"  # este é o site que iremos utilizar para obter os valores dos commodities

# usaremos um 'FOR' para obtermos os valores de cada ITEM da lista do arquivo importado
for item in df_commodities.index:
    produto = df_commodities.loc[item, "Produto"]  # Captura cada valor de cada célula da coluna A (nome do produto)
    # print(produto)
    # o comando a seguir substitui os caracteres especiais deste nome, para que possamos usar na URL
    produto = produto.replace('ó', 'o').replace('ã', 'a').replace('ç', 'c').replace('ú', 'u').replace('é', 'e').replace(
        'á', 'a')

    link = f"https://www.melhorcambio.com/{produto}-hoje"  # agrega o nome do produto ao LINK
    navegador.get(link)  # acessa o link na instancia do navegador que criamos anteriormente
    preco = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute(
        'Value')  # captura o valor do commoditie
    preco = preco.replace('.', '').replace(',', '.')  # padroniza 'ponto' e 'virgula' do valor
    # print(preco)

    df_commodities.loc[item, "Preço Atual"] = float(preco)  # transforma o valor padronizado em 'float'

df_commodities["Comprar"] = df_commodities["Preço Atual"] < df_commodities["Preço Ideal"]  # Atualiza a coluna "Comprar" no nosso DF

print(df_commodities)

df_commodities.to_excel("commodities_mod.xlsx", index=False) # salva o nosso DF em um novo arquivo xlsx