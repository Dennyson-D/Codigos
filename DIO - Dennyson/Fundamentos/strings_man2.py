nome = 'Dennyson'
profissao = 'programador'
idade = 38
cidade = 'Curitiba'

dados = {'nome':'Dennyson', 'idade':38 }

print('meu nome é %s, profissao %s, moro em %s, tenho %i anos' % (nome,profissao,cidade,idade) )

print('meu nome é {}, profissao {}, moro em {}, tenho {} anos'.format(nome,profissao,cidade,idade) )

print('meu nome é {1}, profissao {0}, moro em {3}, tenho {2} anos'.format(profissao,nome,idade,cidade) )

print('meu nome é {no}, profissao {prof}, moro em {cid}, tenho {id} anos'.format(prof=profissao,no=nome,id=idade,cid=cidade) )

print('meu nome é {nome}, tenho {idade} anos'.format(**dados) )