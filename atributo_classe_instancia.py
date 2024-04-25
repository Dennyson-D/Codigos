class Estudante:
    escola = 'DIO'

    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"nome: {self.nome} -  matricula: {self.matricula} - escola: {self.escola}"

def mostrar_aluno(*objts):
    for obj in objts:
         print(obj)

aluno1 = Estudante('Den',1)
aluno2 = Estudante('Dani',2)

mostrar_aluno(aluno1, aluno2)

Estudante.escola = 'ddd'
aluno1.matricula = 4

mostrar_aluno(aluno1,aluno2)
