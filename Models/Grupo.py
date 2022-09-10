class Grupo ():

    def __init__(self, id, alunos):
        self.id = id
        self.alunos = alunos
    
    def __str__(self):
        return f"Grupo {self.id}: {self.alunos}"

    def add_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def remove_aluno(self, aluno):
        self.alunos.remove(aluno)
    
    def set_alunos_nota(self, alunos, nota):
        for aluno in alunos:
            aluno.set_nota(nota)
