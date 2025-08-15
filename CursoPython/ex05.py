#Exercício Python 5:
# Faça um programa que leia um número Inteiro
# e mostre na tela o seu sucessor e seu
# antecessor.
N1 = int
while True:
    while N1 == int:
        N1 = int(input('DIGITE UM NUMERO: '))
        print(f'seu antecessor é {N1 - 1} e seu sucessor é {N1 + 1} !')
    if N1 != int:
        break

print('obrigado')