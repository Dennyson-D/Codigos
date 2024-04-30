def decorador_principal(funcao):
    def envelope():
        print('antes da função')
        funcao()
        print('depois da função')

    return envelope



#decorador
@decorador_principal
def ola():
    print('olá mundo!')

#Forma de chamar decorador, mas não é muito usual, substituida pela forma acima com '@'
#ola = decorador_principal(ola)

ola()