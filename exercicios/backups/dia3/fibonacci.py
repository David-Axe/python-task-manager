#Peca um numero N e mostre os N primeiros numeros da sequencia de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34... (cada numero e a soma dos dois anteriores)

n = int(input('Quantos números da sequência de Fibonacci deseja conhecer? '))

anterior = 0
atual = 1

for i in range(n):
    if i == 0:
        print(0)
    elif i == 1:
        print(1)
    else:
        proximo = anterior + atual
        print(proximo)
        anterior = atual
        atual = proximo
