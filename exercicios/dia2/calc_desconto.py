#Uma loja tem a seguinte regra de desconto:
#Compras ate R$100: sem desconto
#Compras de R$100 a R$500: 10% de desconto
#Compras acima de R$500: 20% de desconto
# Peca o valor da compra e mostre o desconto e o valor final.
valor = float(input('Qual foi o valor da sua compra? '))

if valor <= 100:
    print(f'Você deve pagar R${valor}. Sua compra não teve desconto...')
elif valor <=500:
    desconto = valor * 10 / 100
    print(f'Você deve pagar R${valor - desconto}. Sua compra teve R${desconto:.2f} de desconto!')
else:
    desconto = valor * 20 / 100
    print(f'Você deve pagar R${valor - desconto}. Sua compra teve R${desconto:.2f} de desconto!')

