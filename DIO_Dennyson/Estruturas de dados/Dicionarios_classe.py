#fromkeys
pessoas = {'nome':'Dennyson'}
pessoas.fromkeys(['email','idade'],'valor padrão')
#pessoas['email'] = 'den@gmail.com'

teste = dict.fromkeys(['id','idade'],'vazio')

#print(teste)

for chave, valor in pessoas.items():
    print(chave,valor)
