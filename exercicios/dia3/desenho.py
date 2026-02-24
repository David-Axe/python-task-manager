#Peca um numero N e desenhe um triangulo:
#N = 5:
#*
#**
#***
#****
#*****
#Bonus: Desenhe tambem um triangulo invertido e um losango.

n = int(input('Digite o tamanho dos triângulos e do losângulo: '))

print('Triângulo:')
for i in range(1, n + 1):
    print('*' * i)

print('Triângulo invertido:')
for i in range(n, 0, -1):
    print('*' * i)

print('Losango:')
for i in range(1, n + 1):
    print('*' * i)
for i in range (n - 1, 0, -1):
    print('' * (n - i) + '*' * i)