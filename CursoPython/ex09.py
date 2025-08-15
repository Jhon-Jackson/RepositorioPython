#Exercício Python 9:
# Faça um programa que leia um número Inteiro
# qualquer e mostre na tela a sua tabuada.

print('-*'*30)
print(f'{'Tabuada do Falcao':-^60}')
print('-*'*30)
N1 = int(input('Digite um numero: '))
for c in range (1,11):
    print(f' {c} x {N1} = {c*N1} !')
print('Acabou')
