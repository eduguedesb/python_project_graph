import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import tkinter as tk
from PIL import Image, ImageChops
from io import BytesIO

# Configurar o caminho para o driver do Chrome
chrome_driver_path = r'C:\\Users\\WebGlobal28\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe'

# Configurar as opções do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executar em modo headless (sem interface gráfica)
chrome_options.add_argument("--log-level=3")  # Suprimir mensagens de log do console

# Inicializar o driver do Chrome
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Pasta principal onde estão as subpastas com arquivos HTML
root_folder = r'C:\\projetos\\python\\project_graph\\htmls'

# Criar a pasta 'png' na raiz da pasta principal
output_folder = os.path.join(root_folder, 'png')
os.makedirs(output_folder, exist_ok=True)

root = tk.Tk()

# Ocultar a janela principal
root.withdraw()

# Obter largura e altura da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# Fechar a janela principal
root.destroy()

# Mapeamento de resoluções com base no nome da pasta
resolution_mapping = {
    'doughnut_store': (largura_tela, altura_tela),
    'nightingale': (largura_tela, altura_tela),
    'radialtree': (1960, 1960),
    'scatter': (2350, 1350)
    # Adicione outras resoluções conforme necessário
}

# Iterar sobre as subpastas e arquivos na pasta principal
for subdir, dirs, files in os.walk(root_folder):
    if 'png' in subdir:  # Ignorar a pasta de saída
        continue

    # Contagem de arquivos HTML na pasta atual
    html_files = [f for f in files if f.endswith('.html')]
    total_files = len(html_files)
    
    if total_files == 0:
        continue  # Pular para a próxima pasta se não houver arquivos HTML

    processed_files = 0  # Contador de arquivos processados para a pasta atual
    folder_name = os.path.basename(subdir)
    print(f'Iniciando pasta {folder_name} com {total_files} imagens...')

    for filename in html_files:
        processed_files += 1
        percentage_complete = (processed_files / total_files) * 100

        # Mostrar progresso em uma única linha
        print(f'Carregando imagem {processed_files}/{total_files}... ({percentage_complete:.2f}%)', end='\r')

        # Caminho completo do arquivo HTML
        file_path = os.path.join(subdir, filename)

        # Caminho correspondente na pasta de saída (png)
        relative_path = os.path.relpath(subdir, root_folder)
        output_subdir = os.path.join(output_folder, relative_path)

        # Criar a subpasta correspondente na pasta de saída
        os.makedirs(output_subdir, exist_ok=True)

        # Definir a resolução com base no nome da subpasta
        resolution = resolution_mapping.get(folder_name, (1920, 1080))
        driver.set_window_size(*resolution)

        # Caminho completo para salvar o PNG
        output_file_path = os.path.join(output_subdir, filename.replace('.html', '.png'))

        # Abrir o arquivo HTML no navegador
        driver.get(f'file:///{file_path}')

        # Esperar um tempo para garantir que o gráfico seja renderizado
        time.sleep(2)

        # Encontrar o elemento do gráfico (div com ID 'container')
        graph = driver.find_element(By.ID, 'container')

        # Ajustar o tamanho do gráfico para garantir que seja capturado corretamente
        driver.execute_script("arguments[0].style.width = '100%'; arguments[0].style.height = '100%';", graph)
        time.sleep(1)  # Esperar para que o redimensionamento seja aplicado

        # Capturar a imagem do gráfico como PNG
        png = graph.screenshot_as_png

        # Abrir a imagem com o Pillow
        image = Image.open(BytesIO(png))

        # Fazer o crop automático para remover bordas brancas
        bg = Image.new(image.mode, image.size, (255, 255, 255))  # Cria uma imagem de fundo branco
        diff = ImageChops.difference(image, bg)  # Calcula a diferença entre a imagem e o fundo branco
        bbox = diff.getbbox()  # Obtém a bounding box das áreas não-brancas

        if bbox:
            cropped_image = image.crop(bbox)  # Corta a imagem nos limites da bounding box
        else:
            cropped_image = image  # Se não houver bbox, usa a imagem original

        # Salvar a imagem recortada
        cropped_image.save(output_file_path)

    # Mensagem de sucesso para cada pasta ao finalizar todos os arquivos HTML
    print(f'\nImagens da pasta {folder_name} geradas com sucesso!')

# Fechar o driver
driver.quit()
