# Exercício Python 099:
# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é
# o maior.

def Maior(lst):
    maior = max(lst)
    print(f'O maior numero digitado da lista {lst} foi \033[40;35m{maior}\033[m')


n1 = list()
while True:
    n2 = float(input('Digite qual quer numero: '))
    n1.append(n2)
    while True:
        res = str(input('Sair[S], Continuar[C]')).upper()[0]
        if res in 'SC':
            break
            print('erro, digite S para sair')
    if res == 'S':
        break

print('~'*25)
Maior(n1)