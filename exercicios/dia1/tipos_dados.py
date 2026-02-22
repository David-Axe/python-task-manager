#Crie um programa que pede ao usuario um valor e mostra:
#O valor digitado
#O tipo do valor
#O valor convertido para int (se possivel)
#O valor convertido para float (se possivel)
valor = input('Digite algum valor(número): ')
print(
    f'Valor digitado: {valor} \nTipo de valor: {type(valor).__name__} \nValor convertido para int: {int(float(valor))} \nValor convertido para float: {float(valor)}'
)