class Bicicleta:
    def __init__(self,cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('fom fom')
    
    def parar(self):
        print('Parou')
    
    def correr(self):
        print('Run')      

    # def __str__(self): # exemplo para retornar string
    #     return f'Bicicleta cor:{self.cor}, modelo:{self.modelo}, ano:{self.ano}, valor:{self.valor}'

    def __str__(self): # retornar nome da classe
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta('Vermelha','caloi10',2010,2000)
b2 = Bicicleta('verde','Monark',1998,200)

b1.buzinar()
b1.correr()
b1.parar()

# Outra forma de chamar método
Bicicleta.buzinar(b1)

#print(b1.valor,b1.cor,b1.modelo,b1.ano)
print(b1)
# print(b2.__str__())