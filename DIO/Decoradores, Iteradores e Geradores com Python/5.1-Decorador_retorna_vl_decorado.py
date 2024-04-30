def decorador_principal(funcao):
    def envelope(*args,**kwargs):
        print('antes da função')
        resultado = funcao(*args,**kwargs)
        print('depois da função')
        return resultado

    return envelope



#decorador
@decorador_principal
def ola(nome,outro):
    print(f'olá mundo! {nome}, {outro}')
    return nome.upper()

resultado = ola('denny',10)
print(resultado)