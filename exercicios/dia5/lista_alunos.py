#Crie um programa que gerencia uma lista de alunos:

#Adicionar aluno (nome e nota)
#Listar todos (ordenado por nome)
#Mostrar aprovados (nota >= 7)
#Mostrar reprovados (nota < 7)
#Mostrar media da turma
#Use duas listas paralelas (nomes e notas) ou uma lista de listas.

# ============================================
# LISTA DE ALUNOS
# ============================================
# Programa para gerenciar uma lista de alunos com notas.
#
# FUNCIONALIDADES:
# - Adicionar aluno (nome e nota)
# - Listar todos os alunos (ordenado por nome)
# - Mostrar alunos aprovados (nota >= 7)
# - Mostrar alunos reprovados (nota < 7)
# - Calcular média da turma
#
# COMO USAR:
# 1. Execute o programa: python3 lista_alunos.py
# 2. Escolha uma opção do menu
# 3. Siga as instruções na tela
#
# CONCEITOS UTILIZADOS:
# - Listas
# - Dicionários
# - Funções
# - Condicionais
# - Loops
# - List comprehension
# - String formatting
# ============================================

alunos = []

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    nome = nome.title()
    nota = float(input("Digite a nota do aluno: "))
    alunos.append({'nome': nome, 'nota': nota})
    print(f"Aluno {nome} adicionado com sucesso!")

def listar_todos():
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    
    alunos_ordenados = sorted(alunos, key=lambda x: x['nome'])
    print("\n=== Lista de Todos os Alunos ===")
    for aluno in alunos_ordenados:
        print(f"Nome: {aluno['nome']} - Nota: {aluno['nota']}")

def mostrar_aprovados():
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    
    aprovados = [a for a in alunos if a['nota'] >= 7]
    if not aprovados:
        print("Nenhum aluno aprovado!")
        return
    
    print("\n=== Alunos Aprovados ===")
    for aluno in aprovados:
        print(f"Nome: {aluno['nome']} - Nota: {aluno['nota']}")

def mostrar_reprovados():
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    
    reprovados = [a for a in alunos if a['nota'] < 7]
    if not reprovados:
        print("Nenhum aluno reprovado!")
        return
    
    print("\n=== Alunos Reprovados ===")
    for aluno in reprovados:
        print(f"Nome: {aluno['nome']} - Nota: {aluno['nota']}")

def mostrar_media():
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    
    media = sum(a['nota'] for a in alunos) / len(alunos)
    print(f"\n=== Média da Turma ===")
    print(f"Média: {media:.2f}")

def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Adicionar aluno")
        print("2. Listar todos")
        print("3. Mostrar aprovados")
        print("4. Mostrar reprovados")
        print("5. Média da turma")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            listar_todos()
        elif opcao == "3":
            mostrar_aprovados()
        elif opcao == "4":
            mostrar_reprovados()
        elif opcao == "5":
            mostrar_media()
        elif opcao == "6":
            print("Programa encerrado!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
