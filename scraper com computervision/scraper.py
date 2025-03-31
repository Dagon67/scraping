import pyautogui
import cv2
import time
import numpy as np
import pyperclip
import json
import os

# Configurações dos pontos de clique e do caminho da imagem
image_to_find = cv2.imread(r'C:\Users\PIPA\Documents\ah\figurinha.jpg')
point1 = (1192, 196)  # Coordenadas do primeiro clique
point2 = (5, 202)     # Coordenadas do segundo clique

# Inicializa o JSON para salvar o conteúdo da área de transferência
json_file = 'print2.json'
data = []

# Verifica se o arquivo JSON existe e carrega seu conteúdo
if os.path.exists(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

def find_image_on_screen(image):
    """Procura a imagem na tela e retorna True se encontrada, False caso contrário."""
    screenshot = pyautogui.screenshot()
    screen_np = np.array(screenshot)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
    
    # Converte a imagem alvo para escala de cinza
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplica a correspondência de modelos para verificar se a imagem está na tela
    result = cv2.matchTemplate(screen_gray, image_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Define o nível de confiança para considerar a imagem encontrada
    loc = np.where(result >= threshold)
    
    # Se houver uma correspondência, retorna True
    return len(loc[0]) > 0

# Espera inicial de 5 segundos
time.sleep(5)

# Loop principal
while True:
    # Clica no primeiro ponto e copia o conteúdo
    pyautogui.click(point1)
    time.sleep(0.5)  # Pausa para garantir que o clique seja registrado
    pyautogui.hotkey('ctrl', 'c')  # Simula Ctrl+C
    time.sleep(0.5)  # Pausa para dar tempo ao sistema copiar
    
    # Obtém o conteúdo da área de transferência
    clipboard_content = pyperclip.paste()
    
    # Adiciona o conteúdo ao JSON
    data.append(clipboard_content)
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

    # Clica no segundo ponto e realiza o scroll
    pyautogui.click(point2)
    time.sleep(0.5)  # Pausa para garantir o clique
    pyautogui.scroll(-1)  # Scroll para cima; use -5 para baixo se necessário
    time.sleep(0.2)  # Intervalo entre movimentos de scroll
    
    # Verifica se a imagem foi encontrada na tela
    if find_image_on_screen(image_to_find):
        print("Imagem encontrada na tela! Encerrando o programa.")
        break
