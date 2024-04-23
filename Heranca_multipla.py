class Animal():
     def __init__(self, num_patas):
        self.num_patas = num_patas

     def __str__(self):
         return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"   

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Leao(Mamifero):
    def __init__(self,num_patas):
        self.num_patas = num_patas
        super().__init__(num_patas)

class Cachorro(Mamifero):
    def __init__(self,num_patas):
        self.num_patas = num_patas
        super().__init__(num_patas)

class Gato(Mamifero):
    pass      

class Ornitorrinco(Mamifero,Ave):
    pass

''' --  maneira sem **kw nas classes Mamifero e Ave
class Ornitorrinco(Mamifero, Ave):
    def __init__(self,numn_patas,cor_pelo,cor_bico):
        super().__init__(numn_patas = numn_patas ,cor_pelo = cor_pelo,cor_bico = cor_bico)
'''

gato = Gato(num_patas = 4,cor_pelo = 'preto')
print(gato)

ornitorrinco = Ornitorrinco(num_patas = 4,cor_pelo = 'marron',cor_bico ='amarelo')
print(ornitorrinco)