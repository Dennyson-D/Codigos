letras = list('python')
frutas  = ['abacaxi','banana','caju','manga']

print(letras)
print(frutas[0:4])
print(letras[2:])
print(letras[:2])
print(letras[-1:])
print(letras[0:5:2]) # inicio:fim:step
print(letras[::])
print(letras[::-1])

for id,fruta in enumerate(frutas):
     print(f'{id} - {fruta}')