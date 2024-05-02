# LAVACAR, CALCULANDO TEMPO DOS CARROS NA LAVAGEM

from datetime import datetime, timedelta

tipo = 'g' # pode ser p, m, g
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo == 'p':
    dt_estimada = data_atual + timedelta(minutes = tempo_pequeno)
    print(f'carro chegou as {data_atual}, e finalizará em {dt_estimada}')
elif tipo == 'm':
    dt_estimada = data_atual + timedelta(minutes = tempo_medio)
    print(f'carro chegou as {data_atual}, e finalizará em {dt_estimada}')
elif tipo =='g':
    dt_estimada = data_atual + timedelta(minutes = tempo_grande)
    print(f'carro chegou as {data_atual}, e finalizará em {dt_estimada}')

horas = datetime(2023,7,25,10,19,20) - timedelta(hours=1)
print(horas.time() )

#só data
print(datetime.now().date())