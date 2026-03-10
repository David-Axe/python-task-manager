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
    status = "APROVADO" if media >= 7 else "REPROVADO"
    
    alunos.append({
        "nome": nome_aluno,
        "notas": [nota1, nota2, nota3],
        "media": media,
        "status": status
    })

# Calcula estatísticas da turma
aprovados = sum(1 for a in alunos if a["media"] >= 7)
reprovados = len(alunos) - aprovados
media_turma = sum(a["media"] for a in alunos) / len(alunos)

# Mostra relatório final
print(f"\n=== Relatorio da Turma {nome_turma} ===")

for i, aluno in enumerate(alunos, 1):
    print(f"{i}. {aluno['nome'].title():<15} - Media: {aluno['media']:.1f}  [{aluno['status']}]")

print(f"\nMedia da turma: {media_turma:.1f}")
print(f"Aprovados: {aprovados} ({aprovados/len(alunos)*100:.1f}%)")
print(f"Reprovados: {reprovados} ({reprovados/len(alunos)*100:.1f}%)")
