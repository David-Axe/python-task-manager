#Enunciado:
#Implemente o jogo da forca:
#Lista de palavras pre-definidas
#Computador escolhe uma aleatoriamente
#Jogador tem 6 tentativas
#Mostre as letras acertadas e as erradas

#Algoritmo:
#1. Criar uma lista de palavras
#2. Sortear uma palavra da lista
#3. Criar variável com 6 tentativas
#4. Criar lista vazia para letras erradas
#5. mostrar palavra oculta (_ _ _ _ _)
#6. enquanto tentativas > 0 e palavra não completas:
    #7. pedir uma letra ao usuário
    #8. se a letra está na palavra:
        #9 mostrar a letra na posição correta
    #10. senão:
        #11. subtrair 1 tentativa e
        #12. adicionar a letra na lista de erradas
    #13. mostrar letras erradas
    #14. mostrar tentativas restantes
#15. se tentativas == 0:
    #16. mostrar 'game over'
#17. se palavra foi descoberta (sem '_'):
    #18. mostrar 'você ganhou'

#Código:


#bibliotecas:
import random

palavras = ['elefante', 'cavalo', 'cruzeiro', 'canguru', 'Inglaterra', 'formiga', 'esmeralda', 'restaurante', 'alfaiate', 'marceneiro']

#variáveis
tentativas = 6
letras_erradas = []
palavra = random.choice(palavras)
palavra_oculta = ['_' for _ in palavra]
print(' '.join(palavra_oculta))


while tentativas > 0 and '_' in palavra_oculta:
    letra = input('Chute uma letra:')
    if letra in palavra:
        if letra in palavra_oculta:
            print('Você já descobriu esta letra!')
        else:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
            print(' '.join(palavra_oculta))
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        print(letras_erradas)
    print(f'Tentativas restantes: {tentativas}')
if tentativas == 0:
    print('Game over!')
elif '_' not in palavra_oculta:
    print('Você GANHOU!')
