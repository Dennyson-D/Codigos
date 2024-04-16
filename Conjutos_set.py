# conjunto de dados,é uma lista com números distintos e sem ordernar, não existe index

#exemplos
numero = set([1,2,3,4,5,6,7,4,5,8,1])
texto = set('Brasil')
conjunto = set(('a','b','c','d'))
x = {'python','c','java','html'} # modo mais incomum

print(numero)
print(texto)
print(conjunto)
print(x)

# transformar em list para manipular os valores
numero =  list(numero)
print(numero[0])

#usar enumerate pra descobrir indice
for id,y in enumerate(x):
    print(f'{id} - {y}')

