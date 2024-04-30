class Conta:
    def __init__(self, nro_ag, saldo = 0):
        self.nro_ag = nro_ag
        self._saldo = saldo

    def Depositar(self,valor):
        self._saldo += valor    

    def Sacar(self,valor):
        self._saldo -= valor

    def Mostar_saldo(self):
        return self._saldo    

conta = Conta('0001',500)
conta.Depositar(200)
print(conta.nro_ag)
print(conta.Mostar_saldo())