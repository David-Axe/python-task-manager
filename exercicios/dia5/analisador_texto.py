#Peca um texto e mostre:
#Texto original
#Texto em maiusculas
#Texto invertido
#Quantidade de cada vogal
#Texto sem vogais

#1. Programa deve receber informação (texto) do usuário;
#2. Processar o valor recebido para transformar em saída texto com tudo maiúsculo (função upper) e outras saída texto com tudo minúsculo (função lower).
#3. Processar novamente o texto original para inverter a ordem dos caracteres (fatiamento texto [::-1])
#4. Contabilizar as vogais (.count()) separadamente.
#5. Substituir vogais por ('') usando .replace.

# =============================================================================
# ANALISADOR DE TEXTO
# =============================================================================
# 
# Este programa recebe um texto do usuário e o analisa de várias formas:
#   - Mostra o texto original
#   - Converte para MAIÚSCULAS
#   - Converte para minúsculas
#   - Inverte a ordem dos caracteres
#   - Conta a quantidade de cada vogal (a, e, i, o, u)
#   - Remove todas as vogais do texto
#
# Como usar:
#   Execute o programa e digite qualquer texto quando solicitado.
#   O programa mostrará todas as análises automaticamente.
#
# Exemplo de uso:
#   Entrada: "Ola Mundo"
#   Saída:   Texto original: Ola Mundo
#            Maiúsculas: OLA MUNDO
#            Minúsculas: ola mundo
#            Invertido: odnuM alO
#            Quantidade de vogais:
#              a: 1, e: 0, i: 0, o: 2, u: 1
#            Sem vogais: l mnd
#
# =============================================================================

def converter_maiusculas(texto):
    return texto.upper()


def converter_minusculas(texto):
    return texto.lower()


def inverter_texto(texto):
    return texto[::-1]


def contar_vogais(texto):
    texto_lower = texto.lower()
    return {
        'a': texto_lower.count('a'),
        'e': texto_lower.count('e'),
        'i': texto_lower.count('i'),
        'o': texto_lower.count('o'),
        'u': texto_lower.count('u')
    }


def remover_vogais(texto):
    texto_lower = texto.lower()
    for vogal in 'aeiou':
        texto_lower = texto_lower.replace(vogal, '')
    return texto_lower


def analisar_texto(texto):
    print(f"Texto original: {texto}")
    print(f"Maiúsculas: {converter_maiusculas(texto)}")
    print(f"Minúsculas: {converter_minusculas(texto)}")
    print(f"Invertido: {inverter_texto(texto)}")

    vogais = contar_vogais(texto)
    print(f"Quantidade de vogais:")
    print(f"  a: {vogais['a']}")
    print(f"  e: {vogais['e']}")
    print(f"  i: {vogais['i']}")
    print(f"  o: {vogais['o']}")
    print(f"  u: {vogais['u']}")

    print(f"Sem vogais: {remover_vogais(texto)}")


texto_usuario = input("Digite um texto: ")
analisar_texto(texto_usuario)
