#Pegue o exercicio 2.5 (pedra-papel-tesoura) e refatore usando funcoes:
#pedir_jogada() - pede e valida a jogada do usuario
#jogada_computador() - gera jogada aleatoria
#determinar_vencedor(jogada1, jogada2) - retorna quem ganhou
#jogar() - funcao principal que orquestra o jogo

import random

def pedir_jogada():
    print("1 - PEDRA")
    print("2 - PAPEL")
    print("3 - TESOURA")
    jogada = int(input("Escolha: "))
    while jogada not in [1, 2, 3]:
        jogada = int(input("Inválido. Escolha 1, 2 ou 3: "))
    return jogada

def jogada_computador():
    return random.randint(1, 3)

def determinar_vencedor(usuario, maquina):
    if usuario == maquina:
        return "empate"
    elif (usuario == 1 and maquina == 3) or (usuario == 2 and maquina == 1) or (usuario == 3 and maquina == 2):
        return "usuario"
    else:
        return "maquina"

def jogar():
    print("### PEDRA, PAPEL, TESOURA... ###")
    
    usuario = pedir_jogada()
    maquina = jogada_computador()
    
    opcoes = {1: 'PEDRA', 2: 'PAPEL', 3: 'TESOURA'}
    print(f"{opcoes[usuario]} x {opcoes[maquina]}")
    
    resultado = determinar_vencedor(usuario, maquina)
    
    if resultado == "empate":
        print("Empatou!")
    elif resultado == "usuario":
        print("Você venceu!")
    else:
        print("O computador venceu!")

jogar()
