"""Script para dados do site da B3 com dados do pregão D-1."""
from datetime import datetime, timedelta
import os
import requests
import zipfile

# Calcula a data do dia -1
data_d_1 = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')

# url_pegrões
url = f'https://arquivos.b3.com.br/rapinegocios/tickercsv/{data_d_1}'


# Cria a pasta pregoes com a subpasta da data
pasta = f'pregoes/{data_d_1}'
os.makedirs(pasta, exist_ok=True)

# Faz o download do arquivo
response = requests.get(url)
arquivo = os.path.join(pasta, 'ticker.zip')

# Salva o arquivo na pasta
with open(arquivo, 'wb') as file:
    file.write(response.content)

    # Abre o arquivo zip e extrai o conteúdo
    with zipfile.ZipFile(arquivo, 'r') as zip_ref:
        zip_ref.extractall(pasta)

# Deleta o arquivo .zip
os.remove(arquivo)
