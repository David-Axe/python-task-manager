#Crie funcoes para:
#calcular_media(numeros) - recebe uma lista, retorna a media
#calcular_maior(numeros) - retorna o maior (sem usar max())
#calcular_menor(numeros) - retorna o menor (sem usar min())

#calcular_media
def calcular_media(numeros):
    soma = 0
    for n in numeros:
        soma = soma + n
    return soma / len(numeros)

#calcular_maior
def calcular_maior(numeros):
    maior = numeros[0]
    for n in numeros:
        if n > maior:
            maior = n
    return maior

#calcular_menor
def calcular_menor(numeros):
    menor = numeros[0]
    for n in numeros:
        if n < menor:
            menor = n
    return menor

#loop para preencher a lista (exercicio 'somador')
numeros = []
while True:
    valor = float(input('Digite algum número: '))
    if valor == 0:
        break
    numeros.append(valor)

#chamar as funções
print(f'Média: {calcular_media(numeros)}')
print(f'Maior: {calcular_maior(numeros)}')
print(f'Menor: {calcular_menor(numeros)}')