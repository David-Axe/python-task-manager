#Crie um quiz com pelo menos 5 perguntas:
#Mostre a pergunta e 4 alternativas
#O usuario escolhe a resposta
#Ao final, mostre a pontuacao e quais acertou/errou
#Armazene perguntas em uma lista de listas ou dicionarios

# Quiz com 5 perguntas
perguntas = [
    {
        "pergunta": "1. Qual a capital do Brasil?",
        "alternativas": ["a) Rio de Janeiro", "b) São Paulo", "c) Brasília", "d) Belo Horizonte"],
        "resposta": 3
    },
    {
        "pergunta": "2. Quanto é 2 + 2?",
        "alternativas": ["a) 3", "b) 4", "c) 5", "d) 6"],
        "resposta": 2
    },
    {
        "pergunta": "3. Qual cor é o céu?",
        "alternativas": ["a) Verde", "b) Azul", "c) Vermelho", "d) Amarelo"],
        "resposta": 2
    },
    {
        "pergunta": "4. Quantos dias tem uma semana?",
        "alternativas": ["a) 5", "b) 6", "c) 7", "d) 8"],
        "resposta": 3
    },
    {
        "pergunta": "5. Qual animal late?",
        "alternativas": ["a) Gato", "b) Vaca", "c) Cachorro", "d) Pato"],
        "resposta": 3
    }
]

acertos = 0
resultados = []

print("=== QUIZ ===\n")

for item in perguntas:
    print(item["pergunta"])
    for alt in item["alternativas"]:
        print(alt)
    
    resposta = int(input("Digite a resposta (1-4): "))
    
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
