tarefas = []

def adicionar_tarefa(tarefas):
    titulo = input('Nova tarefa: ')
    titulo = titulo.strip()

    if titulo == '':
        print('Erro: título não pode ficar vazio!')
        return
    
    prioridade = input('Qual é a prioridade da tarefa (alta/média/baixa): ')
    prioridade = prioridade.strip().lower()

    prioridade_validas = ['alta', 'média', 'baixa']
    if prioridade not in prioridade_validas:
        print('Erro: prioridade inválida!')
        return

    tarefa = {
        'titulo': titulo,
        'concluida': False,
        'prioridade': prioridade
    }

    tarefas.append(tarefa)
    print('Tarefa adicionada!')


def mostrar_menu():
    print('''
          =====================================
                  GERENCIADOR DE TAREFAS
          =====================================
          1. Adicionar tarefa
          2. Listar tarefas
          3. Marcar como concluída
          4. Remover tarefa
          5. Sair
          =====================================
        ''')
    
mostrar_menu()