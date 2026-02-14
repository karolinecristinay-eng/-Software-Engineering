class Matricula:
    def __init__(self, ra, nome, curso):
        self.ra = ra
        self.nome = nome
        self.curso = curso
        self.status = "Ativa"

    def __str__(self):
        return f"RA: {self.ra} - {self.nome} ({self.curso}) - {self.status}"


class Tarefa:
    def __init__(self, id, titulo, responsavel, prioridade):
        self.id = id
        self.titulo = titulo
        self.responsavel = responsavel
        self.prioridade = prioridade
        self.status = "Pendente"

    def __str__(self):
        return f"[{self.id}] {self.titulo} - {self.responsavel} ({self.status})"


# Lista global de tarefas
tarefas = []


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for t in tarefas:
            print(t)


def atualizar_status(id_tarefa):
    for t in tarefas:
        if t.id == id_tarefa:
            t.status = "Concluido"
            print(f"Tarefa {id_tarefa} atualizada!")
            return
    print("Tarefa não encontrada.")


def menu():
    while True:
        print("\n1. Criar Tarefa\n2. Listar\n3. Concluir\n4. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            id = int(input("ID: "))
            titulo = input("Título: ")
            responsavel = input("Responsável: ")
            prioridade = input("Prioridade: ")
            tarefas.append(Tarefa(id, titulo, responsavel, prioridade))
            print("Tarefa criada com sucesso!")

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            id_tarefa = int(input("ID da tarefa a concluir: "))
            atualizar_status(id_tarefa)

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


# Executar menu
menu()
