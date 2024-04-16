#exemplos

pessoa = {'Nome':'Dennyson','Idade':38}
pessoa  =  dict(Nome = 'Dennyson', Idade = 38)
carro = {'Nome':'Prisma', 'marca': 'gm'}
pc = dict(cpu = 'Ryzen7 5800x3d', moba = 'tuf', gabinete = 'x-strike biturbo', placa_video = 'rtx 3060')
pc['fonte'] = 'ax850'

'''
print(pessoa['Nome'])
print(pc['cpu'])
print(carro['Nome'])
'''
# exemplo contatos
contatos = {
'email1@gmail.com':{'nome':'nome1','idade': 30,'chave':{'a':123}},
'email2@gmail.com':{'nome':'nome2','idade':25,'chave':{'a':456}},
'email3@gmail.com':{'nome':'nome3','idade':35,'chave':{'a':987}}    
}

nome1 = contatos['email1@gmail.com']['nome'] 
chave1 = contatos['email1@gmail.com']['chave']['a']

#forma1
for chave in contatos:
    print( chave,contatos[chave])

#forma2 - mais legivel
for chave,valor in contatos.items():
    print(chave,valor)