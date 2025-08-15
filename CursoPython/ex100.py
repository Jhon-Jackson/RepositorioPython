# Exercício Python 100:
# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro
# da lista e a segunda função vai mostrar a soma entre todos
# os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista):
    c = 1
    # for c in range(0,5):
    while c <= 5 :
        aleat = randint(0,len(lista)-1)

        if lista[aleat] not in sort:
            sort.append(lista[aleat])
            c += 1
    print(f'\nLista com 5 numeros Sorteada ',end='')
    for cc, v in enumerate(sort):
        print(v,end=' ')


def somaPar(lista):
    som = 0
    for i, v in enumerate(lista):
        if v % 2 == 0:
            som += v
    print(f'\nA soma dos pares é {som}')

cont = 1
Num = list()
sort = list()
while cont <= 10:
    n1 = randint(0, 100)
    if n1 not in Num:
        Num.append(n1)
        cont += 1
print('-='*35)
sorteia(Num)
print()
somaPar(sort)
