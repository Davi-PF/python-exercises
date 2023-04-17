## Exercício 6 - Gerador de Senhas
#   Escreva um gerador de senhas em python. Seja criativo com a forma de gerar senhas - senhas fortes possuem uma mistura de letras minúsculas, maiúsculas, números e símbolos. 
#   As senhas devem ser aleatórias, gerando uma nova senha a cada vez que o usuário executar o programa.

import random
import string

# Define os caracteres disponíveis para a senha
caracteres = string.ascii_letters + string.digits + string.punctuation

# Define o tamanho da senha
tamanho = 16

# Gera a senha aleatória
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

# Exibe a senha gerada
print("Sua senha é:", senha)