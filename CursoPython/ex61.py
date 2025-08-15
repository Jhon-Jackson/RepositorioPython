#Exercício Python 61:
# Refaça o DESAFIO 51, lendo o primeiro
# termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando
# a estrutura while.

P = int(input('PRIMEIRO TERMO: '))
R = int(input('A RAZAO: '))
termo = P
cont = 1
while cont <= 10:
    print(f'{termo} ->',end='')
    termo = termo + R
    cont += 1
print('FIM')
