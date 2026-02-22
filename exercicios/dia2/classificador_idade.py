#Peca a idade e classifique:
#0-12: Crianca
#13-17: Adolescente
#18-59: Adulto
#60+: Idoso

idade = int(input('Quantos anos você tem? '))
if idade <= 12:
    print('Você ainda é uma criança!')
elif idade <= 17:
    print('Então você é um(a) adolescente!')
elif idade <= 59:
    print('Você já é um(a) adulto!')
else:
    print('Você alcançou uma idade respeitável, já está idoso(a)!') 