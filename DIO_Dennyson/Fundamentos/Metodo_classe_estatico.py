class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod  # transofrma em método de classe
    def criar_por_dt_nascimento(cls,ano,mes,dia,nome):  # conveção para @classmethod é 'cls'
        idade = 2024-ano
        return Pessoa(nome,idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    
p1 = Pessoa('Denny',38)

p2= Pessoa.criar_por_dt_nascimento(1986,2,1,'Dennyson')

print(p2.nome, p2.idade)
print(p2.maior_idade(p2.idade))