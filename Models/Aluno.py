class Aluno():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.nota = 0
        self.matricula = matricula
        self.grupo = None
    
    def __str__(self):
        return f"{self.nome} - {self.matricula}"
    
    def set_nota(self, nota):
        self.nota = nota
    
    def set_grupo(self, grupo):
        self.grupo = grupo
    