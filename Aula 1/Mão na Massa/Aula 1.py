''' Este é um código desenvolvido por mim através de um intensivo de Python ministrado pela
 Hashtag Treinamentos e tem o intuito de:
 - Mostrar o funcionamento da bibliotecas:
    > pyautogui -> controlar mouse e teclado
    > pyperclip -> copiar e colar textos neste exemplo
    > pandas    -> Analise de dados
    > time      -> utilizada para criar delays neste exemplo

 E como objetivo final será enviado um email contendo uma análise de dados simples, através das seguintes
 etapas:
 - Abrir uma nova página no navegador;
 - Acessar a página que contém o relatório para análise (página simplificada);
 - Extração do relatório;
 - Analise de dados através do arquivo baixado;
 - Abertura do email;
 - Criação e envio do email contendo os dados da análise.
'''

import pyautogui
import time
import pandas as pd
import pyperclip

# pyautogui.click()
# pyautogui.write()
# pyautogui.press()
# pyautogui.hotkey()
# pyautogui.position()

pyautogui.PAUSE = 0.5 # Determina o delay após cada comando do pyautogui

# 1º Passo: Entrar no sistema
# https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema


pyautogui.click(x=121, y=756) # clica no ícone do Edge na MINHA barra de iniciar
pyautogui.hotkey("ctrl", "t") # Atalho para abrir uma nova guia
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema") # Escreve a URL
                                                                        # no campo de URL do navegador
pyautogui.press("enter") # Pressiona enter para navegar até a URL
time.sleep(2) #aguarda 2 segundos


pyautogui.click(x=589, y=379) # clica no campo do login
pyautogui.write("Login")    # digita o login fictício

pyautogui.press("tab")      # passa p/ o campo da senha
pyautogui.write("senha")    # digita a senha fictícia

pyautogui.press("tab")      # seleciona o botão 'entrar'
pyautogui.press("enter")    # aperta o botão 'entrar'

time.sleep(3) #aguarda 3 segundos

pyautogui.click(x=475, y=453)   # seleciona o arquivo
pyautogui.click(x=1133, y=198)  # abre o menu
#pyautogui.click(x=889, y=656)   # clica em download

time.sleep(2) #aguarda 2 segundos

tabela = pd.read_csv(r"C:\Users\SEU_USUARIO_AQUI\Downloads\Compras.csv", sep=';') #importa o arquivo que
                                            # fizemos o download anteriormente no site

total_gasto = tabela['ValorFinal'].sum()    # realiza a soma da coluna 'ValorFinal'
quantidade = tabela['Quantidade'].sum()     # realiza a soma da coluna 'Quantidade'
preco_medio = total_gasto / quantidade      # Divide o total gasto pela quantidade, assim
                                            # obtemos o preço médio


pyautogui.click(x=495, y=47)                # clica na barra de pesquisar do navegador
pyautogui.write("https://outlook.live.com/mail/0/") # escreve o endereço do outlook
pyautogui.press("enter")                    # aperta enter para acessar o outlook
time.sleep(5)                               #aguarda 5 segundos

pyautogui.click(x=177, y=212)               #clica em 'Novo email'
time.sleep(4)                               #aguarda 4 segundos
pyautogui.write("Insira seu email aqui")    #Insere o email do destinatário
pyautogui.press("tab")                      # confirma o email
pyautogui.press("tab")                      # passa para o assunto

assunto_email = "Relatório de Vendas"       #Cria uma variavel com o nome do assunto
pyperclip.copy(assunto_email)               #Usa a biblioteca para que não se percam os caract. especiais
pyautogui.hotkey("ctrl", "v")               #O famoso 'Ctrl + V'
pyautogui.press("tab")                      #passa para o corpo do email

#A seguinte variavel cria o corpo do email
corpo_email = f'''                          
Prezados,
Segue o relatório de compras

Total gasto: R${total_gasto:,.2f}
Quantidade de produtos: R${quantidade:,}
Preço Médio: R${preco_medio:,.2f}
'''

pyperclip.copy(corpo_email)             #Copia o texto da variavel acima
pyautogui.click(x=731, y=438)           #Clica no campo 'corpo do email'
pyautogui.hotkey("ctrl", "v")           #O famoso 'Ctrl + V'
pyautogui.hotkey("ctrl", "enter")       # envia o email