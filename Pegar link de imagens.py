import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.gettyimages.pt/fotos/'

nomes = [nome for nome in os.listdir('.') if (nome.endswith('jpg') or nome.endswith('png') or nome.endswith('JPG') or nome.endswith('PNG'))and (nome.startswith('gett'))]
nomes

codigos = []
for nome in nomes:
    codigo_nome = nome[nome.find('-')+1:nome.rfind('-')]
    codigos.append(codigo_nome)
codigos

cont = 0
with open('Links_imagens.txt', 'w') as f:
    for cod in codigos:
        source = requests.get(url + cod).text
        soup = BeautifulSoup(source, "html.parser")
        links = soup.find_all('a')
        for link in links:
            classe = link.get('class')
            if classe == ['gallery-mosaic-asset__link'] or classe == ['search-result-asset-link']:
                f.write('https://www.gettyimages.pt' + link.get('href')+'\n')
                cont+=1
    f.write(f'\nTotal de links encontrados: {cont}')