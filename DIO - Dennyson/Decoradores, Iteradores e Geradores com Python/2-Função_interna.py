def principal():
    print('executando a função princiapl')

    def funcao_interna():
        print('func interna')

    def funcao2():
        print('executando func 2')

    funcao_interna()
    funcao2()

principal()