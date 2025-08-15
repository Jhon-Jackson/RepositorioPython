#Exercício Python 086:
# Crie um programa que declare uma matriz de
# dimensão 3×3 e preencha com valores lidos
# pelo teclado. No final, mostre a matriz na
# tela, com a formatação correta.

Matrix = [[],[],[]], [[],[],[]], [[],[],[]]
zero = um = dois = c = 0
for c in range (0,3):
    zero = int(input(f'Digite um valor: [0:{c}] '))
    Matrix[0][c].append(zero)
for c in range (0,3):
    um = int(input(f'Digite um valor: [1:{c}] '))
    Matrix[1][c].append(um)
for c in range(0, 3):
    dois = int(input(f'Digite um valor: [2:{c}] '))
    Matrix[2][c].append(dois)
print('=-'*30)
#print(Matrix)
for c in range (0, 3):
    print(f'[{Matrix[0][c]:^5}]',end='')
print()
for c in range (0, 3):
    print(f'[{Matrix[1][c]:^5}]',end='')
print()
for c in range (0, 3):
    print(f'[{Matrix[2][c]:^5}]',end='')
