import os
import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configurações do ChromeDriver
chrome_options = Options()

# Diretório base de download
download_directory = "C:\\Users\\walve\\Documents\\FIAP\\Fase 2 BigData\\Tech Challenge\\Tech_Challenge_2\\pregoes"

# Configurações do ChromeDriver para o diretório de download
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Nome do arquivo no formato IBOVDia_dd-mm-aa.csv
today_date = datetime.today().strftime('%d-%m-%y')
file_name = f'IBOVDia_{today_date}.csv'
downloaded_file_path = os.path.join(download_directory, file_name)

# Verifica se o arquivo já existe
if not os.path.exists(downloaded_file_path):
    # Inicializa o ChromeDriver
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)

    # Acessa a URL desejada
    url = "https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br"
    driver.get(url)

    # Aguarda o carregamento da página
    time.sleep(5)

    # Encontra e clica no botão de download (ajuste o seletor conforme necessário)
    # Ajuste o texto do link conforme necessário
    download_button = driver.find_element(By.LINK_TEXT, 'Download')
    download_button.click()

    # Aguarda o download ser concluído
    time.sleep(10)

    # Fecha o navegador
    driver.quit()

    # Lê o arquivo CSV ignorando a primeira linha e as duas últimas, usando a codificação 'latin1'
    df = pd.read_csv(downloaded_file_path, skiprows=1, encoding='latin1')
    df = df[:-2]

    # Salva o DataFrame como um arquivo Parquet
    parquet_file_path = os.path.join(
        download_directory, f'IBOVDia_{today_date}.parquet')
    df.to_parquet(parquet_file_path)
    
else:
    print(f"O arquivo {file_name} já existe. O download foi cancelado.")
