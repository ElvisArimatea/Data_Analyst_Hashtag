'''
Este código tem a simples função de capturar a localização X/Y do mouse
'''

import pyautogui
import time

time.sleep(3)                   #Aguarda 3 segundos, para que possamos ir até o local desejado
print(pyautogui.position())     #Captura e imprime no terminal a localização do mouse
