#Exercício Python 67:
# Faça um programa que mostre a tabuada de
# vários números, um de cada vez, para cada
# valor digitado pelo usuário.
# O programa será interrompido quando o
# número solicitado for negativo.
from time import sleep
N = c = cont = soma = 0
while True:
    N = int(input('Voce quer ver tabuada de qual numero? '))
    if N < 0 :
        break
    for cont in range (1 ,11):
        sleep(1)
        soma = cont * N
        print(f'{N} x {cont} = {soma}')
        cont += 1
print('Fim')