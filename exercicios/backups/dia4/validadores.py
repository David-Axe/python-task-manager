#Crie funcoes que retornam True ou False:
#e_palindromo(texto) - "ana" e palindromo, "casa" nao
#e_primo(numero) - 7 e primo, 8 nao
#e_email_valido(email) - precisa ter @ e . depois do @

#palindromo
def verificar_palindromo(texto):
    if texto == texto[::-1]:
        return True
    return False

#numero primo
def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

#e-mail
def verificar_email(texto):
    if '@' not in texto:
        return False
    posicao_arroba = texto.find('@')
    return '.' in texto[posicao_arroba:]