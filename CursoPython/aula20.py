# Nessa aula,
# vamos aprender o que são funções ou rotinas e como utilizar
# funções em Python. Funções são trechos de código que podem ser
# executados em momentos diferentes de nossos códigos em Python.
# Veja como funciona o comando def em Python e como utilizá-lo com
# parâmetros simples e múltiplos.
# def lin(msg):
#     print('-' *40)
#     print(f'{msg:^40}')
#     print('-' *40)
#
#
# lin('ola, jhon')
# lin('ola, larice')
# lin('ola, samuel')
from random import randint, randint

# def soma(a,b):
#    print(f'A = {a} e B = {b}')
#    s = a + b
#    print(f'A soma A{a} + B{b} = AB{s}')
#
#
# soma(7, 8)

# def contador(*num):
#     for valor in num:
#         tam = len(M)
#         print(f'recebi os valores {valor}', end='')
#         print(f' Ao todo sao {tam} numeros')
#     print('FIM')
# M = []
# for c in range(0,10):
#     N = randint(1,50)
#     M.append(N)
#
# contador(sorted(M))

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2,9,3,6,1,10]
print(valores)
dobra(valores)
print(valores)


