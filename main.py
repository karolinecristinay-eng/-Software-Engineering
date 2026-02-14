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

