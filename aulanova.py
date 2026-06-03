import requests as r
from bs4 import BeautifulSoup

try:
    resultado = r.get('https://www.eb.mil.br/')
except Exception as erro:
    print('erro', erro)
else:
    resposta = resultado.text
    soup = BeautifulSoup(resposta, 'html.parser')

    print(soup.find('h2', class_='portlet-title-text').prettify())