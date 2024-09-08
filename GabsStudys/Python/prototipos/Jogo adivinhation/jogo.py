import os
import random
import time

# Função para limpar o terminal
def limpar_terminal():
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para macOS e Linux
        os.system('clear')

# Função para animação de escolha do número
def animacao_escolha():
    print("O PC está escolhendo um número", end="")
    for _ in range(3):
        time.sleep(0.7)  # Pausa de 0.7 segundos para criar o efeito
        print(".", end="", flush=True)
    print("\n")

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Limpa o terminal e exibe a introdução
limpar_terminal()
print(""" 
*****************************************
* Bem vindo ao jogo da adivinhation lek *
*****************************************
""")

# Animação antes de iniciar o jogo
animacao_escolha()

# Primeira tentativa do jogador
numero_chute0 = int(input("Qual seu chute campeão? "))

# Verifica o resultado da primeira tentativa
if numero_chute0 == numero_secreto:
    print("Parabéns tiozao, vc adivinhou!")
else:
    # Segunda tentativa
    numero_chute1 = int(input("Não, tente mais uma vez: qual seu 2° chute meu rei? "))
    if numero_chute1 == numero_secreto:
        print("Parabéns tiozao, vc adivinhou!")
    else:
        # Terceira tentativa
        numero_chute2 = int(input("Poxa, ainda não é este, última chance chefe: "))
        if numero_chute2 == numero_secreto:
            print("Parabéns tiozao, vc adivinhou!")
        else:
            # Limpa o terminal e exibe o resultado final
            limpar_terminal()
            print(f"""Que pena! você gastou todas suas tentativas.
O número secreto era {numero_secreto}...
Suas tentativas foram: {numero_chute0}, {numero_chute1} e {numero_chute2}""")
