## Exercício 2 - Palíndromos
#   Peça uma string qualquer ao usuário e informe a ele se a string é um palíndromo ou não. 
#   (um palíndromo é uma string que pode ser lida da mesma forma, da esquerda para a direita ou vice-versa. Ex.: *omo*).

def verificarPalindromo(word):
    # Remove espaços e transforma tudo para minúsculas
    word = word.replace(' ', '').lower()
    # Verifica se a palavra é igual à sua forma invertida
    return word == word[::-1]

palavra = input('Digite uma palavra: ')

if verificarPalindromo(palavra):
    print(f"{palavra} é um palíndromo!")
else:
    print(f"{palavra} não é um palíndromo.")