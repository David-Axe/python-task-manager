#Faca um jogo contra o computador:
#Usuario digita sua escolha
#Computador escolhe aleatoriamente (import random)
#Programa diz quem ganhou

import random
titulo = '### PEDRA, PAPEL, TESOURA... ###'
print(f'{titulo:^50}')
usuario = int(input(
    'Escolha umas das opções abaixo: \n'
    '1 - PEDRA \n' \
    '2 - PAPEL \n' \
    '3 - TESOURA \n'
))
maquina = random.randint(1, 3)
opcoes = {1: 'PEDRA', 2: 'PAPEL', 3: 'TESOURA'}

print('Pedra, papel, tesoura...:')
if usuario == maquina:
    print(f'{opcoes[usuario]} x {opcoes[maquina]}')
    print('Empatou')
elif (usuario == 1 and maquina == 3) or (usuario == 2 and maquina == 1) or (usuario == 3 and maquina == 2):
    print(f'{opcoes[usuario]} x {opcoes[maquina]}')
    print('Venceu!!!')
else:
    print(f'{opcoes[usuario]} x {opcoes[maquina]}')
    print('Vitória do computador!')