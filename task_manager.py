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
