#Exercício Python 088:
# Faça um programa que ajude um jogador da
# MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo em uma lista
# composta.
from random import randint
from time import sleep
jogo = []
numaleat = 0
print('=-'*30)
print(f'{'JOGO DA MEGA SENA':^60}')
print('=-'*30)
palpite = int(input('Voce quer  quantos palpites de jogo: '))
print('-='*3, f'SORTEANDO {palpite} JOGOS','-='*3)
cont = 0
for cn in range (1, palpite +1):
    for c in range (0,6):
        numaleat = randint(1, 60)
        jogo.append(numaleat)
        if numaleat == jogo:
            jogo.remove(numaleat)
    while True:
        if numaleat not in jogo:
            numaleat = randint(1, 60)
            jogo.append(numaleat)
            if numaleat != jogo:
               break
    sleep(0.5)
    jogo.sort()
    print(f'JOGO {cn}: {jogo}')
    jogo.clear()
print('-='*5, '< BOA SORTE >', '-='* 5)

