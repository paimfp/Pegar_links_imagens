import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.gettyimages.pt/fotos/'

nomes = [nome for nome in os.listdir('.') if (nome.endswith('jpg') or nome.endswith('png') or nome.endswith('JPG') or nome.endswith('PNG'))and (nome.startswith('gett'))]

codigos = []
for nome in nomes:
    codigo_nome = nome[nome.find('-')+1:nome.rfind('-')]
    codigos.append(codigo_nome)

cont = 0
with open('Links_imagens.txt', 'w') as f:
    for cod in codigos:
        source = requests.get(url + cod).text
        soup = BeautifulSoup(source, "html.parser")
        for link in soup.find_all('link'):
            if link.get('hreflang') == 'pt-BR':
                f.write(link.get('href')+'\n')
                cont+=1
                break
    f.write(f'\n\nTotal de links encontrados: {cont}')