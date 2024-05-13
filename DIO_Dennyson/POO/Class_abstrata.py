from abc import ABC, abstractmethod, abstractproperty

class Controle_remoto(ABC):
     @abstractmethod
     def ligar(self):
          pass
     
     @abstractmethod
     def desligar(self):
          pass

     @property
     @abstractproperty
     def marca(self):
          pass

class Controle_tv(Controle_remoto): # classe filha precisa obrigatóriamente implementar os métodos abstratos, no caso ligar e desligar
     def ligar(self):
          print('ligar tv')

     def desligar(self):
          print('desligar tv')     
     @property
     def marca(self):
          return 'LG'     

class Controle_ar(Controle_remoto):
     def ligar(self):
          print('Ligar ar condicionado')

     def desligar(self):
          print('Desligar ar condicionado')    
     @property
     def marca(self):
          return 'Samsumg'                


c = Controle_tv()
c.ligar()
c.desligar()
print(c.marca)

ar = Controle_ar()
ar.ligar()
ar.desligar()
print(ar.marca)