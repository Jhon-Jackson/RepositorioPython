#Exercício Python 060:
# Faça um programa que leia um número
# qualquer e mostre o seu fatorial.
# Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

#from math import factorial
#N = int(input('DIGITE UM NUMERO PARA CALCULAR SEU FACTORIAL: '))
#F = factorial(N)
#print(f'o fatorial de {N} é {F}.')

n = int(input('Digite um numero para calcular seu Fatorial: '))
c = 1
Tot = 1
print(f'Calculando {n}!= ',end='')
for c in range (n,1-1,-1) :
    print(c,end='')
    print(' x ' if c > 1 else ' = ',end='')
    Tot *= c
'''while c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else ' = ', end='')
    Tot *= c
    c -= 1'''
print(f'{Tot}',end='')
