class veiculo():
    def __init__(self,cor,placa,num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print('ligando motor!!!')    

class Motocicleta(veiculo):
    pass

class Carro(veiculo):
    def movimento(self):
        print('o carro está em movimento!')

class Caminhao(veiculo):
    def __init__(self, cor,placa,num_rodas,carregado):        
         super().__init__(cor,placa,num_rodas)   
         self.carregado =  carregado

    def esta_carregado(self):
        print( f"{'carregado' if self.carregado else 'Não carregado'}")


carro = Carro('prata','def-456',4)
moto = Motocicleta('preta','abc-123',2)
caminhao = Caminhao('azul','ghj-789',6, False)

moto.ligar_motor()
carro.movimento()
caminhao.esta_carregado()

print(caminhao.cor)