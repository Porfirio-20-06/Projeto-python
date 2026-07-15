
#cadastro e login
print("Bem-vindo ao sistema de cadastro e login!")
print('Possui um cadastro? (S/N)')

#usuario ja cadastrado
if input().upper() == 'S':
    print("Digite seu email e senha para fazer login.")
    email = input("Email: ")
    senha = input("Senha: ")
    print("Login realizado com sucesso!")

#criação de cadastro
else:
    print("Vamos criar um novo cadastro.")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    print("Cadastro realizado com sucesso!")

#adicionar tarefas
tarefa = []
while True:
    print("Digite uma tarefa para adicionar à lista (ou 'sair' para encerrar):")
    nova_tarefa = input()
    if nova_tarefa.lower() == 'sair':
        break
    tarefa.append(nova_tarefa)
    print(f"Tarefa '{nova_tarefa}' adicionada à lista.")

#editar tarefas
while True:
    print("Deseja editar alguma tarefa? (S/N)")
    if input().upper() == 'N':
        break
    print("Digite o número da tarefa que deseja editar (1 a {}):".format(len(tarefa)))
    numero_tarefa = int(input()) - 1
    if 0 <= numero_tarefa < len(tarefa):
        print("Digite a nova descrição da tarefa:")
        nova_descricao = input()
        tarefa[numero_tarefa] = nova_descricao
        print(f"Tarefa {numero_tarefa + 1} atualizada para: '{nova_descricao}'")
    else:
        print("Número de tarefa inválido.")

#remover tarefas
while True:
    print("Deseja remover alguma tarefa? (S/N)")
    if input().upper() == 'N':
        break
    print("Digite o número da tarefa que deseja remover (1 a {}):".format(len(tarefa)))
    numero_tarefa = int(input()) - 1
    if 0 <= numero_tarefa < len(tarefa):
        tarefa_removida = tarefa.pop(numero_tarefa)
        print(f"Tarefa '{tarefa_removida}' removida da lista.")
    else:
        print("Número de tarefa inválido.")

#marcar tarefas como concluídas
while True:
    print("Deseja marcar alguma tarefa como concluída? (S/N)")
    if input().upper() == 'N':
        break
    print("Digite o número da tarefa que deseja marcar como concluída (1 a {}):".format(len(tarefa)))
    numero_tarefa = int(input()) - 1
    if 0 <= numero_tarefa < len(tarefa):
        tarefa[numero_tarefa] += " (Concluída)"
        print(f"Tarefa {numero_tarefa + 1} marcada como concluída.")
    else:
        print("Número de tarefa inválido.")

#salvar em arquivo json
import json

with open("tarefas.json", "w") as f:
    json.dump(tarefa, f)
