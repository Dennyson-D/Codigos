class Passaro:
    def voar(self):
        print('Voando..')

class Pardal(Passaro):
    def voar(self):
        return super().voar()

class Avestruz(Passaro):            
      def voar(self):
          print('Avestruz não voa')  

class Aviao(Passaro):
    def voar(self):
        print('Avião decolando')          

def plano_voo(obj):
    obj.voar()          



plano_voo(Passaro())
plano_voo(Avestruz())
plano_voo(Aviao())