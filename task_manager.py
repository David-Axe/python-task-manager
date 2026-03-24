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


def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada!')
        return
    
    print('\n --- SUAS TAREFAS ---\n')

    for i, tarefa in enumerate(tarefas, start=1):
        if tarefa['concluida']:
            marca = '[X]'
        else:
            marca = '[ ]'
        print(f"{i}. {marca} {tarefa['titulo']} ({tarefa['prioridade']})")

def marcar_concluida(tarefas):
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada!')
        return
    
    listar_tarefas(tarefas)
    c1 = int(input('Qual tarefa você deseja marcar como concluída? '))
    if c1 < 1 or c1 > len(tarefas):
        print('Número inválido!')
        return
    indice = c1 - 1
    tarefas[indice]['concluida'] = True
    print('Tarefa marcada como concluída!')
        
def remover_tarefa(tarefas):
    if len(tarefas) > 0:
        listar_tarefas(tarefas)
        remove = int(input('Qual tarefa você deseja remover? '))
        if remove < 1 or remove > len(tarefas):
            print('Esta tarefa não existe!')
            return
        indice = remove - 1
        tarefas.pop(indice)
        print('Tarefa removida! ')


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
adicionar_tarefa(tarefas)
listar_tarefas(tarefas)