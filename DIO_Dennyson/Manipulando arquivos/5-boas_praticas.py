from pathlib import Path

ROOTHPATH = Path(__file__).parent

# metodo fechando com o close()
# arquivo = open(ROOTHPATH/'arquivo.txt', 'r')
# arquivo.close()
# print(arquivo.read())

#método boas práticas, ele já fecha automaticamente
try:
    with open(ROOTHPATH/"arquivo.txt") as arq:
        print('trabalhando com arquivo')
# erros genéricos
except IOError as exc:
    print(f'Erro ao abrir o arquivo {exc}')

# print(arq.read())

#enconding
# try:
#     with open(ROOTHPATH/'arq-utf8.txt', 'w',encoding='utf-8') as arquivo:
#         arquivo.write('manipulando arquivo utf8')
# except IOError as exc:
#     print('erro {exc}')        

try:
    with open(ROOTHPATH/'arq-utf8.txt', 'r',encoding='ascii') as arquivo:
        arquivo.read()
except IOError as exc:
    print('erro {exc}')     