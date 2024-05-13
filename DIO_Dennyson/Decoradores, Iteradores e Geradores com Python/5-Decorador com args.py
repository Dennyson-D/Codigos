def decorador_principal(funcao):
    def envelope(*args,**kwargs):
        print('antes da função')
        funcao(*args,**kwargs)
        print('depois da função')

    return envelope



#decorador
@decorador_principal
def ola(nome,outro):
    print(f'olá mundo! {nome}, {outro}')


ola('denny','outro')