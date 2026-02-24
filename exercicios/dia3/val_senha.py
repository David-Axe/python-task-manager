#Crie um programa que pede uma senha e valida:
#Minimo 8 caracteres
#Pelo menos uma letra maiuscula
#Pelo menos um numero. Se a senha for fraca, peca novamente. Se for forte, aceite.

print('Vamos criar uma senha!')
print('Ela deve ter no mínimo 8 caracteres, pelo menos uma letra maiúscula, pelo menos um número')

while True:
    senha = input('Digite a senha: ')

    valida_tamanho = len(senha) >= 8
    valida_maiuscula = any(c.isupper() for c in senha)
    valida_numero = any(c.isdigit() for c in senha)

    if valida_tamanho and valida_maiuscula and valida_numero:
        print('Senha forte! Aceita!')
        break
    else:
        print('Senha fraca! Tente novamente!')
        if not valida_tamanho:
            print('Precisa de pelo menos 8 caracteres!')
        if not valida_maiuscula:
            print('Precisa de pelo menos uma letra maiúscula!')
        if not valida_numero:
            print('Precisa de pelo menos um número!')