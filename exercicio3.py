# Exercício 3 - Pedra, Papel, Tesoura
# Faça um jogo de *pedra, papel ou tesoura* de dois jogadores. 
# (Dica: peça as jogadas ao usuário - usando `input` - compare-os, imprima uma mensagem parabenizando o vencedor e pergunte ao usuário se quer continuar jogando).

while True:
    # Solicita as jogadas dos jogadores
    jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ")
    jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ")

    # Verifica quem ganhou ou se houve empate
    if jogador1 == jogador2:
        print("Empate!")
    elif jogador1 == "pedra":
        if jogador2 == "papel":
            print("Jogador 2 ganhou!")
        else:
            print("Jogador 1 ganhou!")
    elif jogador1 == "papel":
        if jogador2 == "tesoura":
            print("Jogador 2 ganhou!")
        else:
            print("Jogador 1 ganhou!")
    elif jogador1 == "tesoura":
        if jogador2 == "pedra":
            print("Jogador 2 ganhou!")
        else:
            print("Jogador 1 ganhou!")
    else:
        print("Jogada inválida. Tente novamente.")

    # Pergunta se o usuário quer continuar jogando
    jogar_novamente = input("Quer jogar novamente? (s/n) ")
    if jogar_novamente.lower() != "s":
        break