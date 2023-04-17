## Exercício 7 - Leitura de arquivos

# Dado um arquivo `.txt` que contem uma lista de nomes, conte quantas vezes cada nome aparece no arquivo e imprima os resultados na tela. 
# Um arquivo `nomes.txt` é fornecido junto a esse repositório.

from collections import Counter

# Abre o arquivo e lê os nomes
with open('names.txt', 'r') as f:
    nomes = f.read().split()

# Conta a ocorrência de cada nome
contador_nomes = Counter(nomes)

# Imprime os resultados
for nome, ocorrencias in contador_nomes.items():
    print(f'{nome}: {ocorrencias}')