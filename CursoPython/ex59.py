#Exercício Python 059:
# Crie um programa que leia dois valores e
# mostre um menu na tela:

#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
# #[ 5 ] sair do programa
#Seu programa deverá realizar a operação
# solicitada em cada caso.
from time import sleep
N1 = int(input('DIGITE UM NUMERO: '))
N2 = int(input('DIGITE OUTRO NUMERO: '))
Opc = 0
while Opc != 5:
    Sair = 5
    Somar = N1 + N2
    Mult = N1 * N2
    Maior = 0
    Opc = 0
    sleep(1)
    print('''Escolha uma opção desejada 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior numero
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa.''')
    Opc = int(input('Escolha uma opção: '))
    if Opc == 1 :
        print(f'A soma dos valores {N1} + {N2} é {Somar}..')
    elif Opc == 2:
        print(f'O Multiplo dos valores {N1} x {N2} é {Mult}.')
    elif Opc == 3:
        if N1 > N2:
            Maior = N1
        elif N2 > N1 :
            Maior = N2
        print(f'O maior numero entre os valores {N1} e {N2} é {Maior}.')
    elif Opc == 4:
            print('Informe os novos valores: ')
            N1 = int(input('DIGITE UM NUMERO: '))
            N2 = int(input('DIGITE OUTRO NUMERO: '))
    else:
        print('opção invalida, tente novamente!')
print('Até Mais Volte sempre !!')
