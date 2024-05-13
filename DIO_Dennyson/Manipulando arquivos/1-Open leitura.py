# o padrão é o 'r' leitura, mesmo que não coloque o 'r', mas é melhor deixar explicito

#ler todo conteude de uma vez
arquivo = open('arquivo.txt', 'r')
print(arquivo.read())

#ler com readlines
for linha in arquivo.readlines():
    print(linha)

#para ler com readline
while len(linha := arquivo.readline()):
    print(linha)
arquivo.close()