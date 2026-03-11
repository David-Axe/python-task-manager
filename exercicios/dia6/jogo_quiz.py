#Crie um quiz com pelo menos 5 perguntas:
#Mostre a pergunta e 4 alternativas
#O usuario escolhe a resposta
#Ao final, mostre a pontuacao e quais acertou/errou
#Armazene perguntas em uma lista de listas ou dicionarios

# ALGORITMO JogoQuiz
# 1. Criar lista de perguntas (cada pergunta tem: texto, 4 alternativas, resposta correta)
# 2. Inicializar variável acertos = 0
# 3. Inicializar lista resultados = vazia
# 4. Para cada pergunta na lista:
#    a. Mostrar o texto da pergunta
#    b. Mostrar as 4 alternativas
#    c. Pedir resposta do usuário (a, b, c ou d)
#    d. Se resposta for inválida (não é a, b, c ou d):
#       - Mostrar mensagem de erro
#       - Pedir resposta novamente até ser válida
#    e. Converter resposta para minúscula
#    f. Se resposta == resposta_correta:
#       - acertos = acertos + 1
#       - adicionar "Acertou" na lista resultados
#    g. Senão:
#       - adicionar "Errou" na lista resultados
# 5. Mostrar pontuação final (acertos de total de perguntas)
# 6. Para cada pergunta:
#    a. Mostrar o número da pergunta e se acertou/errou
# FIM

# ============================================================================
# README - JOGO QUIZ
# ============================================================================
#
# DESCRIÇÃO:
# Este programa é um jogo de quiz interativo com 5 perguntas de múltipla
# escolha, onde o usuário responde e recebe feedback sobre seu desempenho.
#
# FUNCIONALIDADES:
# 1. Exibir 5 perguntas com 4 alternativas cada (a, b, c, d)
# 2. Coletar resposta do usuário
# 3. Validar entrada (apenas a, b, c ou d)
# 4. Converter resposta para minúscula (tratamento de maiúsculas)
# 5. Contabilizar acertos automaticamente
# 6. Mostrar pontuação final
# 7. Listar cada pergunta com resultado (Acertou/Errou)
#
# ESTRUTURA DE DADOS:
# - Lista de dicionários contendo: pergunta, alternativas[], resposta
#
# TRATAMENTO DE ERROS:
# - Validação de entrada (apenas a, b, c, d)
# - Conversão .lower() para aceitar maiúsculas/minúsculas
# - Loop while para pedir nova entrada se inválida
#
# ============================================================================

# Quiz com 5 perguntas
perguntas = [
    {
        "pergunta": "1. Qual a capital do Brasil?",
        "alternativas": ["a) Rio de Janeiro", "b) São Paulo", "c) Brasília", "d) Belo Horizonte"],
        "resposta": "c"
    },
    {
        "pergunta": "2. Quanto é 2 + 2?",
        "alternativas": ["a) 3", "b) 4", "c) 5", "d) 6"],
        "resposta": "b"
    },
    {
        "pergunta": "3. Qual cor é o céu?",
        "alternativas": ["a) Verde", "b) Azul", "c) Vermelho", "d) Amarelo"],
        "resposta": "b"
    },
    {
        "pergunta": "4. Quantos dias tem uma semana?",
        "alternativas": ["a) 5", "b) 6", "c) 7", "d) 8"],
        "resposta": "c"
    },
    {
        "pergunta": "5. Qual animal late?",
        "alternativas": ["a) Gato", "b) Vaca", "c) Cachorro", "d) Pato"],
        "resposta": "c"
    }
]

acertos = 0
resultados = []

print("=== QUIZ ===\n")

for item in perguntas:
    print(item["pergunta"])
    for alt in item["alternativas"]:
        print(alt)
    
    resposta = input("Digite a resposta (a-d): ").lower()
    
    while resposta not in ["a", "b", "c", "d"]:
        print("Opção inválida! Digite apenas a, b, c ou d")
        resposta = input("Digite a resposta (a-d): ").lower()
    
    if resposta == item["resposta"]:
        acertos += 1
        resultados.append("Acertou")
    else:
        resultados.append("Errou")
    
    print()

print("=== RESULTADO ===")
print(f"Você acertou {acertos} de {len(perguntas)} perguntas\n")

for i, item in enumerate(perguntas):
    print(f"{i+1}. {item['pergunta'][:30]}... - {resultados[i]}")
