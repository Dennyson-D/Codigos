cores = ['azul','amarelo','verde','vermelho','preto']
cor1 = []

for cor in cores:
    if 'a' in cor:
        cor1.append(cor)
print(cor1)     

# comprehension
cor1 = [cor for cor in cores if 'a' in cor]
print(cor1)


# outro exemplo
numeros = [1,2,3,4,5,6,7,8,9,10]
quadrado = [numero**2 for numero in numeros]
print(quadrado)