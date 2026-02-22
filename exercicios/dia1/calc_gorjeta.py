#Peca o valor da conta e o percentual de gorjeta desejado. Mostre: valor da gorjeta, total com gorjeta, e valor por pessoa (pergunte quantas pessoas).
print('Então vamos fechar a conta!')
quantidade = int(input('Quantas pessoas? '))
valor_conta = float(input('Qual é o valor da conta? '))
gorjeta = float(input('Quantos por cento deseja dar de gorjeta? '))
gorjeta_valor = valor_conta * (gorjeta / 100)
total = valor_conta + gorjeta_valor
valor_por_pessoa = total / quantidade
print(
    f'Valor da Gorjeta: R${gorjeta_valor:.2f} \nValor total: R${total:.2f} \nValor por pessoa R${valor_por_pessoa:.2f}'
)


