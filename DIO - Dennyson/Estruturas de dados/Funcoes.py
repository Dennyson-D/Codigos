def mensagem():
    print('Função')

def mensagem2(nome):
    print(f'Bem vindo {nome}')

def mensagem3(nome  = 'anonimo'):
    print(f'Olá {nome}')

def calculos(num):
    print (sum(num))

def numeros(num):
    ant = num - 1
    pro = num + 1
    return ant,pro

def carro(ano,modelo,marca,placa):
    print(f'carro ano {ano}, modelo {modelo}, marca {marca} placa {placa}')


# mensagem()
# mensagem2(nome = 'Dennyson')    
# mensagem3()
# mensagem3(nome = 'Jaspion')

# calculos([5,3,2])
# print(numeros(10))

#forma que segue em ordem de itens declarados
carro(2000,'Prisma','GM','ABC-1234')

#forma declarando variaveis
carro(modelo = 'Prisma', placa = 'ABC-1234', ano = 2016, marca = 'GM')

#forma dicionário
carro(**{'ano':2014,'marca':'GM','modelo':'Prisma','placa':'ABC-1234'})

