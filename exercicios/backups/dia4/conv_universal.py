#Crie funcoes de conversao:
#celsius_para_fahrenheit(c)
#fahrenheit_para_celsius(f)
#km_para_milhas(km)
#milhas_para_km(milhas)
#kg_para_libras(kg) Monte um menu que permite ao usuario escolher qual conversao quer.

def celsius_para_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9

def km_para_milhas(km):
    return km * 0.621371

def milhas_para_km(mi):
    return mi * 1.60934

def kg_para_libras(kg):
    return kg * 2.20462

def libras_para_kg (lb):
    return lb * 0.45359237

print('1. Celsius para Fahrenheit')
print('2. Fahrenheit para Celsius')
print('3. km para milhas')
print('4. Milhas para km')
print('5. kg para libras')
print('6. Libras para kg')

opcao = input('Escolha: ')

if opcao == '1':
    valor = float(input('Digite a temperatura em Celsius: '))
    print(f'{celsius_para_fahrenheit(valor):.2f}')
elif opcao == '2':
    valor = float(input('Digite a temperatura em Fahrenheit: '))
    print(f'{fahrenheit_para_celsius(valor):.2f}')
elif opcao == '3':
    valor = float(input('Digite a distância em km: '))
    print(f'{km_para_milhas(valor):.2f}')
elif opcao == '4':
    valor = float(input('Digite a distância em milhas: '))
    print(f'{milhas_para_km(valor):.2f}')
elif opcao == '5':
    valor = float(input('Digite o peso em kg: '))
    print(f'{kg_para_libras(valor):.2f}')
elif opcao == '6':
    valor = float(input('Digite o peso em libras: '))
    print(f'{libras_para_kg(valor):.2f}')
else:
    print('Opção inválida')
