#Exercício Python 47:
# Crie um programa que mostre na tela todos
# os números pares que estão no intervalo
# entre 1 e 50.
from time import sleep
#exemplo 01
#for cont in range(2,52,2):
    #print(cont,end=',')
#exemplo 02
for cont in range(2,52,2):
    if cont % 2 == 0:
        print(f'\033[34m{cont}\033[m',end=',')
        sleep(0.5)