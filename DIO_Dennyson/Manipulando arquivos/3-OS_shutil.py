import os,shutil
from pathlib import Path

#pegar o endereço do arquivo
ROOT_PATH = Path(__file__).parent

# os.mkdir(ROOT_PATH / 'Novo-diretorio')

# arquivo = open('novo-arquivo.txt', 'w')

#criar arquivo txt dentro do novo diretório
arquivo = open(ROOT_PATH /'Novo-diretorio/novo.txt', 'w')

arquivo.close()

#para alterar nomes
# os.rename(ROOT_PATH/'novo.txt', ROOT_PATH/'alterado.txt')

#remover arquivo
# os.remove(ROOT_PATH/'alterado.txt')

#mover arquivod e diretório
open('mover.txt', 'w')
shutil.move('mover.txt', ROOT_PATH/'Novo-diretorio')