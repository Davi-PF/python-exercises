## Exercício 5 - Remover duplicatas

# Escreva um programa que receba uma lista e retorne uma nova lista que contenha todos os elementos da primeira lista, menos as duplicadas.
def remove_duplicatas(lista):
    nova_lista = []
    for elemento in lista:
        if elemento not in nova_lista:
            nova_lista.append(elemento)
    return nova_lista

lista = [1, 2, 3, 3, 4, 4, 5, 'a', 'a', 'b', 'c', 'd', 'd', 'e', 'f', 'a']
nova_lista = remove_duplicatas(lista)
print(f"Lista antiga: {lista}")
print(f"Lista nova: {nova_lista}")
