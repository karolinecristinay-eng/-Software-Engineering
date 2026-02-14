class Tarefa:
    def __init__(self, id, titulo, responsavel, prioridade):
        self.id = id
        self.titulo = titulo
        self.responsavel = responsavel
        self.prioridade = prioridade
        self.status = "Pendente"

    def __str__(self):

        return f"[{self.id}] {self.titulo} - {self.responsavel} ({self.status})"
class Tarefa:
    def __init__(self, id, titulo, responsavel, prioridade):
        self.id = id
        self.titulo = titulo
        self.responsavel = responsavel
        self.prioridade = prioridade
        self.status = "Pendente"

    def __str__(self):
        return f"[{self.id}] {self.titulo} - {self.responsavel} ({self.status})"
    def listar_tarefas():
        if not tarefas:
            print("Nenhuma tarefa encontrada.")
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
        if opcao == "4": break
        



