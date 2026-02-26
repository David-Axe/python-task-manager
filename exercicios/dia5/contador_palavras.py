# Enunciado:
# Peça uma frase e mostre:
# - Número de palavras
# - Número de caracteres (com e sem espaços)
# - Palavra mais longa
# - Palavra mais curta

# ========================
# README - Contador de Palavras
# ========================

# Objetivo:
# Este programa analisa uma frase digitada pelo usuário e exibe:
# 1. Quantidade de palavras na frase
# 2. Quantidade de caracteres (incluindo espaços)
# 3. Quantidade de caracteres (sem contar espaços)
# 4. A palavra mais longa da frase
# 5. A palavra mais curta da frase

# Conceitos utilizados:
# - input(): recebe dados do usuário via terminal
# - split(): divide uma string em lista, usando espaços como separador
# - len(): retorna o número de elementos (caracteres ou palavras)
# - replace(" ", ""): Remove todos os espaços da string
# - max()/min(..., key=len): encontra maior/menor elemento baseado no comprimento

# Exemplo de execução:
# Entrada: "Python é uma linguagem poderosa"
# Saída:
#   Número de palavras: 5
#   Número de caracteres (com espaços): 28
#   Número de caracteres (sem espaços): 24
#   Palavra mais longa: poderosa
#   Palavra mais curta: é

# Código:
frase = input("Digite uma frase: ")

palavras = frase.split()

num_palavras = len(palavras)
num_caracteres_com_espacos = len(frase)
num_caracteres_sem_espacos = len(frase.replace(" ", ""))

palavra_mais_longa = max(palavras, key=len)
palavra_mais_curta = min(palavras, key=len)

print(f"Número de palavras: {num_palavras}")
print(f"Número de caracteres (com espaços): {num_caracteres_com_espacos}")
print(f"Número de caracteres (sem espaços): {num_caracteres_sem_espacos}")
print(f"Palavra mais longa: {palavra_mais_longa}")
print(f"Palavra mais curta: {palavra_mais_curta}")
