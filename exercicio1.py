## Exercício 1 - Par ou Ímpar
# Peça ao usuário um número. Retorne a ele se o número é par ou impar.
num = int(input('Digite um numero: '))

if(num % 2 == 0):
    print(f'O numero {num} e par!')
elif(num % 2 != 0):
    print(f'O numero {num} e impar!')