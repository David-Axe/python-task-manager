#Crie um programa que converte Celsius para Fahrenheit e vice-versa.
#Formula: F = C * 9/5 + 32
#Pergunte ao usuario qual conversao quer fazer
linha = '*'*50
title = 'CONVERSOR DE TEMPERATURA\n'

print(linha)
print(f'{title:^50}')
print('Escolha a conversão:')
print('1 - Celsius para Fahrenheit')
print('2 - Fahrenheit para Celsius\n')
print(linha,'\n')
opcao = input('Digite 1 ou 2: ')

if opcao == '1':
    c = float(input('Quantos graus Celsius? '))
    f = c * 9 / 5 + 32
    print(f'{c}ºC = {f:.2f}ºF')
elif opcao == '2':
    f = float(input('Quanto graus Fahrenheit? '))
    c = (f - 32) * 5 / 9
    print(f'{f}ºF = {c:.2f}ºC')
else:
    print('Opção inválida!')

