#Peca um numero e mostre a tabuada completa (1 a 10).

numero = int(input('A tabuada de qual número você deseja conhecer? '))
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
