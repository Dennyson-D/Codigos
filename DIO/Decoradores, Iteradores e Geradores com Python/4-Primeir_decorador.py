def decorador_principal(funcao):
    def envelope():
        print('antes da função')
        funcao()
        print('depois da função')

    return envelope

def ola():
    print('olá mundo!')

#decorador
ola = decorador_principal(ola)
ola()    