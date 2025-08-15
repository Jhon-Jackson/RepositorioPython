#Exercício Python 73:
# Crie uma tupla preenchida com os 20
# colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois
# mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

time = ('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional','São Paulo',
        'Corinthians','Bahia','Cruzeiro','Vasco da Gama','EC Vitória','Atlético-MG',
        'Fluminense','Grêmio','Juventude','Bragantino','Athletico-PR','Criciúma',
        'Atlético-GO','Cuiabá')
print('-*' * 15)
print(f'lista de times do Brasileirao: {time}')
print('-*' * 15)
print(f'times em ordem alfabetica:{sorted(time)}')
print('-*' * 15)
print(f'os 5 primeiros times do brasieirao:{time[0:5]}')
print('-*' * 15)
print(f'os 4 ultimos colocados do brasileirao: {time[-4:]}')
print('-*' * 15)
print(f'a posição do time Cruzeiro esta {time.index('Cruzeiro')+1}ªposição')