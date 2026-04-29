#Peca 3 valores e verifique:
#Se formam um triangulo (cada lado deve ser menor que a soma dos outros dois)
#Se sim, diga se e equilatero (3 iguais), isosceles (2 iguais) ou escaleno (todos diferentes)
titulo = 'VERIFICADOR DE TRIANGULO'
print(f'{titulo:^50}')
a = float(input('Digite um número: '))
b = float(input('Digite um outro número: '))
c = float(input('Digite um terceiro número: '))
if a < b + c and b < a + c and c < a + b:
    print('Estas medidas fornecidas podem formar um triângulo!')
    if a == b == c:
        print('Este é um triângulo equilatero!')
    elif a == b or b == c or a == c:
        print('Este é um triângulo isosceles')
    else:
        print('Este é um triângulo escaleno!')
else:
    print('Não é possível formar um triângulo com estas medidas!')
