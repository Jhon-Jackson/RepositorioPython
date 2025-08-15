#Exercício Python 091:
# Crie um programa onde 4 jogadores joguem um dado e tenham
# resultados aleatórios. Guarde esses resultados em um dicionário
# em Python. No final, coloque esse dicionário em ordem, sabendo
# que o vencedor tirou o maior número no dado.

from random import randint
import time
from operator import itemgetter, itemgetter

# jogo = {'jogador1': randint(1,6),
#         'jogador2': randint(1,6),
#         'jogador3': randint(1,6),
#         'jogador4': randint(1,6)}
# ranking = list()
# print('Valores sorteados: ')
# for k , v in jogo.items():
#     print(f'{k} tirou {v} no dado. ')
#     time.sleep(1)
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print()
# for i , v in enumerate(ranking):
#     print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
#     time.sleep(1)

jogadores = {}
jogo = []
ranking = list()

for c in range(1,5):
    dado = randint(1, 6)
    jogadores[f"jogador{c}"]  = dado
jogo.append(jogadores.copy())
# print(jogo)
print('-='*40)
for kv in jogo:
    for k, v in kv.items():
        print(f'o {k} tirou {v} no dado.')
        time.sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('-='*40)
for i , v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    time.sleep(1)
