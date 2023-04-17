## Exercício 9 - Gravar um arquivo

# Pegue o código do exercício anterior e ao invés de imprimir os resultados na tela, escreva-os em um arquivo txt. No seu código você
# pode deixar o nome do arquivo *hard-coded*.


## Exercício 8
# Use os pacotes `BeautifulSoup` e `requests` para imprimir uma lista de todos os títulos de artigos do [New York Times](http://www.nytimes.com/).

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.content, features='html.parser')

titles = [h3.text.strip() for h3 in soup.find_all('h3', {'class': 'indicate-hover'})]

with open('nytimes_titles.txt', 'w') as f:
    for title in titles:
        f.write(title.strip() + '\n')