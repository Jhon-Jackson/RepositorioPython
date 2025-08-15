#Exercício Python 45:
# Crie um programa que faça o computador
# jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
comp = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Qual é sua jogada: '))
print('JO..')
sleep(1)
print('KEM..')
sleep(1)
print('POO!!!')
print('\033[34m@'*30)
print(f'\033[32mcomputador jogou {itens[comp]}\033[m')
print(f'\033[33mjogador jogou {itens[jog]}\033[m')
print('\033[34m@'*30)
if comp == 0 :
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('jogador venceu'.upper())
    elif jog == 2:
        print('computador venceu'.upper())
elif comp == 1:
    if jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('JOGADOR VENCEU')
    elif jog == 0:
        print('COMPUTADOR VENCEU')
elif comp == 2:
    if jog == 0:
        print('JOGADOR VENCEU')
    elif jog == 1:
        print('COMPUTADOR VENCEU')
    elif jog == 2:
        print('EMPATE')

#print(f'o computador escolhe {itens[comp]}')