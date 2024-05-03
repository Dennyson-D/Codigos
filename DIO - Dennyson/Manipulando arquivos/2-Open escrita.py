# cria o arquivo 'texte.txt'
arquivo = open('teste.txt', 'w')

#escrevendo no arquivo
arquivo.write('testando escrevar no arquivo.')

#escrevendo com writelines
arquivo.writelines(['\nPython ', '\num ', '\nnovo ', '\ntexto.'])


arquivo.close()