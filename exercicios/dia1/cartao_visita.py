#Crie um programa que pede nome, profissao, telefone e email, e imprime um cartao formatado:

#=============================
#        JOAO SILVA
#     Desenvolvedor Python
#  Tel: (47) 99999-9999
#  Email: joao@email.com
#=============================
print('Olá! Vamos fazer um cartão digital para você!')
nome = input('Qual é o seu nome completo? ')
nome = nome.upper()
profissao = input('Qual é a sua profissão? ')
profissao = profissao.title()
telefone = input('Qual é o seu número de telefone? (com DDD) ')
tel = 'Tel.:'
email = input('Qual é o seu e-mail? ')
email = email.lower()
emailtitle = "E-mail:"
linha = '='*50
print(
    f'{linha}\n'
    f'{nome:^50}\n'
    f'{profissao:^50}\n'
    f'{tel + telefone:^50}\n'
    f'{emailtitle + email:^50}\n'
    f'{linha}\n'
)