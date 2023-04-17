## Exercício 4 - Jogo da adivinhação
# Gere um número aleatório entre 1 e 9 (incluindo 1 e 9).
# Peça ao usuário para adivinhar o número, e então diga se a tentativa foi menor, maior ou correta. 
# (Dica: lembre-se de usar o `input` dos exercícios anteriores). Mantenha o jogo executando até que o usuário digite "sair".

import random

while True:
    # Gera um número aleatório entre 1 e 9
    numero = random.randint(1, 9)

    # Pede ao usuário para adivinhar o número
    palpite = input("Adivinhe o número entre 1 e 9 (ou digite 'sair' para encerrar o jogo): ")

    # Verifica se o usuário quer encerrar o jogo
    if palpite.lower() == "sair":
        break

    # Converte a entrada do usuário em um número inteiro
    palpite = int(palpite)

    # Verifica se o palpite do usuário é menor, maior ou correto
    if palpite < numero:
        print("Seu palpite foi menor.")
    elif palpite > numero:
        print("Seu palpite foi maior.")
    else:
        print("Parabéns! Você acertou o número!")

print("Obrigado por jogar!")