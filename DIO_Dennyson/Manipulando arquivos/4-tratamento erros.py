from pathlib import Path

ROOTPATH = Path(__file__).parent

try:
    arquivo = open(ROOTPATH/'meu_arq.txt')
except FileNotFoundError as exc:
    print('arquivo não encontrado')
    print(exc)

try:
    arquivo = open(ROOTPATH/'Novodir')
except IsADirectoryError as exc:
    print(f'Erro diretório: {exc}')
#exeçãos em detalhes
except Exception as exc:
    print(f'Houve algum problema. {exc}')

