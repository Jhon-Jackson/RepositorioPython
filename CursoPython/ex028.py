from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador "pensar"
print("-=-" * 20)
print('vou sorterar um numero de 0 a 5 , Tente adivinhar...')
print('-=-'* 20)
jogador = int(input(' Em que numero vou Sortear? ')) # jogador vai tentar adivinhar
print('HMMM Seraa?')
sleep(2)
if jogador == computador:
    print('Paraben ! Voce conseguiu me vencer! ')
else:
    print(f'Ganhei ! Eu sorteei o numero {computador} e nao no {jogador}!')
