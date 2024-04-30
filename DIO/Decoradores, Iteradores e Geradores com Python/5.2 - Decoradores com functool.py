import functools
# functools serve para deixar nome da função correto
def decorador_principal(funcao):
    @functools.wraps(funcao)
    def envelope(*args,**kwargs):
        funcao(*args, **kwargs)

    return envelope


@decorador_principal
def ola(nome,outro):
    print(f'olá mundo! {nome}, {outro}')

ola('Denny',100)
print(ola.__name__)