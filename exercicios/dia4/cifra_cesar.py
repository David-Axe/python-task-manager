#Crie uma funcao que criptografa texto deslocando cada letra por N posicoes:
#criptografar("abc", 3) → "def"
#descriptografar("def", 3) → "abc"

def criptografar(texto, n):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''

    for letra in texto:
        if letra in alfabeto:
            posicao = alfabeto.index(letra)
            nova_posicao = (posicao + n) % 26
            resultado += alfabeto[nova_posicao]
        else:
            resultado += letra
    return resultado

def descriptografar(texto, n):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''

    for letra in texto:
        if letra in alfabeto:
            posicao = alfabeto.index(letra)
            nova_posicao = (posicao - n) % 26
            resultado += alfabeto[nova_posicao]
        else:
            resultado += letra
    return resultado


print('1. Criptografar')
print('2. Descriptografar')
opcao = input('Escolha: ')

texto = input('Digite o texto: ')
n = int(input('Digite o número de posições (n): '))

if opcao == '1':
    resultado = criptografar(texto, n)
    print(f'Texto criptografado: {resultado}')
elif opcao == '2':
    resultado = descriptografar(texto, n)
    print(f'Texto descriptografado: {resultado}')
else:
    print('Opção inválida')
