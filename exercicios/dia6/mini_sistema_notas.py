#Crie um programa completo que:
#Pede o nome da turma
#Pede quantos alunos tem
#Para cada aluno, pede nome e 3 notas
#Calcula media de cada aluno
#Mostra relatorio final:

# Pede o nome da turma
nome_turma = input("Nome da turma: ")

# Pede quantos alunos tem
qtd_alunos = int(input("Quantos alunos tem na turma: "))

alunos = []

def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"Nota {numero} (0-10): "))
            if 0 <= nota <= 10:
                return nota
            print("Erro: a nota deve estar entre 0 e 10")
        except ValueError:
            print("Erro: digite um número válido")

# Para cada aluno, pede nome e 3 notas
for i in range(qtd_alunos):
    print(f"\n--- Aluno {i + 1} ---")
    nome_aluno = input("Nome do aluno: ")
    
    nota1 = ler_nota(1)
    nota2 = ler_nota(2)
    nota3 = ler_nota(3)
    
    # Calcula média de cada aluno
    media = (nota1 + nota2 + nota3) / 3
    
    # Define status
    status = "Aprovado" if media >= 7 else "Reprovado"
    
    alunos.append({
        "nome": nome_aluno,
        "notas": [nota1, nota2, nota3],
        "media": media,
        "status": status
    })

# Mostra relatório final
print("\n" + "=" * 30)
print(f"TURMA: {nome_turma}")
print("=" * 30)

for aluno in alunos:
    print(f"\nAluno: {aluno['nome'].title()}")
    print(f"Notas: {aluno['notas'][0]}, {aluno['notas'][1]}, {aluno['notas'][2]}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Status: {aluno['status']}")
    print("-" * 20)

