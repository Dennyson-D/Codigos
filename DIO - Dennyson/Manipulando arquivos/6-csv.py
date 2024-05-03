import csv
from pathlib import Path

ROOTPATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1

#criar
# try:
#     with open(ROOTPATH/'usuarios.csv', 'w', newline = '',encoding = 'utf-8') as arq:
#         escritor = csv.writer(arq)
#         escritor.writerow(['id','nome'])
#         escritor.writerow([1,'Denny'])
#         escritor.writerow([2,'Dani'])
#         escritor.writerow([3,'mucuim'])

# except IOError as exc:
#     print(f'errro: {exc}')

#ler 1
# try:
#     with open(ROOTPATH/'usuarios.csv', 'r', encoding = 'utf-8') as arq:
#         leitor = csv.reader(arq)
#         for linha in leitor:
#             print(linha)
# except IOError as exc:
#     print(f'erro: {exc}')

#  outra forma de ler 2
# try:
#     with open(ROOTPATH / 'usuarios.csv', 'r', newline ='', encoding = 'utf-8') as arq:
#         leitor = csv.reader(arq)
#         for row in leitor:
#             print(row[COLUNA_ID], row[COLUNA_NOME])
# except IOError as exc:
#     print(f'erro {exc}')  

# dictreader ler 3

try:
    with open('usuarios.csv', 'r', newline='', encoding = 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['id'], row['nome'])

except IOError as exc:
    print(f'erro {exc}')