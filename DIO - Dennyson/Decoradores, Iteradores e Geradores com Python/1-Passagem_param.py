def mensagem(nome = 'Denny'):
    print('executando msg')
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'olá tudo bem com vc {nome}'

def executar(funcao,nome):
    print('executando')
    return funcao(nome)

print(executar(mensagem,'Dennyson'))

print(executar(mensagem_longa,'Dennyson'))