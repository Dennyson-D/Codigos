x = 'pyTHon'
y = '  pyTHon  '
z = 'Python'

print(x.upper()) #maiúsculas
print(x.lower()) #minúsculas
print(x.title()) #primeira maiúscula
print(y.strip()) # tirar espaços
print(y.lstrip()) # tirar espaço a esquerda
print(y.rstrip()) # tirar espaço direito
print(z.center(20,'#')) # centralizar(segundo item opcional)
print('-'.join(z))