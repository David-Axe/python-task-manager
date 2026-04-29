#Crie um programa com dicionarios que:

#Cadastra alunos (nome, idade, curso)
#Lista todos os alunos
#Busca aluno por nome
#Remove aluno
#Mostra estatisticas (total, media de idade)


alunos = {}

def cadastrar():
    nome = input('Qual o nome do aluno? ')
    idade = int(input('Qual é a idade do aluno? '))
    curso = input('Qual é o curso do aluno? ')
    alunos[nome] = {'idade': idade, 'curso': curso}
    print('Aluno cadastrado com sucesso!')

