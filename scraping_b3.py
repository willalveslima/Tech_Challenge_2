import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configurações do ChromeDriver
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": "C:\\Users\\walve\\Documents\\FIAP\\Fase 2 BigData\\Tech Challenge\\Tech_Challenge_2\\pregoes",  # Altere para o diretório desejado
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Inicializa o ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Acessa a URL desejada
url = "https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br"
driver.get(url)

# Aguarda o carregamento da página
time.sleep(5)


# Encontra e clica no botão de download (ajuste o seletor conforme necessário)
download_button = driver.find_element(By.LINK_TEXT, 'Download')  # Ajuste o texto do link conforme necessário
download_button.click()

# Aguarda o download ser concluído
time.sleep(10)

# Fecha o navegador
driver.quit()