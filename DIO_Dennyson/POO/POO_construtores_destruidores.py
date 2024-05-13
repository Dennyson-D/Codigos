class Cachorro:
    def __init__(self,nome,cor,acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('Removendo instancia da classe')

    def latir(self):
        print('AU AU')    

c1 = Cachorro('Mukuim','marron')

c1.latir()
print(c1.nome)
del(c1)
print('teste')