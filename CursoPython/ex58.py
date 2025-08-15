#Exercício Python 58:
# Melhore o jogo do DESAFIO 28 onde
# o computador vai “pensar” em um número
# entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando
# no final quantos palpites foram
# necessários para vencer.

# ACERTOU = false
#while not ACERTOU:
# if JOG == COMP:
#   ACERTOU = true
from random import randint
from time import sleep
print('-='*30)
print(f'{'''VAMOS JOGAR ADIVINHAÇÃO
VOU ESCOLHER ENTRE 0 A 10 E VOCE TENTA ADIVINHAR''':^100}')
print('-='*30)
COMP = randint (0,10)
cont = 1

JOG = int(input('Escolha um numero jogador: '))
for c in range(0, 3):
    print('.', end='')
    sleep(0.5)
while JOG != COMP:
    if JOG > COMP :
        JOG = int(input('\nMENOS.., TENTE NOVAMENTE : '))
    elif JOG < COMP:
        JOG = int(input('\nMAIS.., TENTE NOVAMENTE : '))
    c = 0
    for c in range (0,3):
        print('.',end='')
        sleep(0.5)
    if JOG == COMP:
        print('\nVOCE GANHOU')
    cont += 1
print(f'computador escolheu {COMP} e voce {JOG} !!')
print(f'TENTATIVAS {cont} vezes')
