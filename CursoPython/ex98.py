# Exercício Python 098:
# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função
# criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
import time
def cont1():
    print('~'*25)
    for c in range (1,11):
        print(c,end=' ')
        time.sleep(0.5)
    print('FIM!')


def cont2():
    print('~' * 25)
    for c2 in range(10,-1,-2):
        print(c2, end=' ')
        time.sleep(0.5)
    print('FIM!')


def cont3(í,f,p):
    print('~' * 25)
    if p < 0:
        p*=-1
    if p == 0:
        p = 1
    for c3 in  range(í,f,p):
        print(c3, end=' ')
        time.sleep(0.5)
    print('FIM!')


cont1()
print()
cont2()
print()

print('~' * 25)
print('Agora é sua vez de personalizar a contagem! ')
inicio = int(input('Inicio: '))
Fim = int(input('Fim: '))
Passo = int(input('Passo: '))
cont3(í=inicio,f=Fim,p=Passo)

