#Peca numeros ao usuario ate ele digitar 0. Ao final, mostre:
#Quantidade de numeros digitados
#Soma total
#Media

print('Digite números para serem somados e tirado uma média. Digite 0 para concluir.')

numeros = []
while True:
    valor = float(input('Digite algum número: '))
    if valor == 0:
        break
    numeros.append(valor)

quantidade = len(numeros)
soma = sum(numeros)
media = soma / quantidade if quantidade > 0 else 0

print(f'Quantidade: {quantidade}')
print(f'Soma: {soma}')
print(f'Média: {media:.2f}')
