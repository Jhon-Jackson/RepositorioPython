#Exercício Python 087:
# Aprimore o desafio anterior, mostrando no
# final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [0,0,0],[0,0,0],[0,0,0]
somap = somat = mail = main = 0
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite o valor na posição [{l}:{c}]:  '))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 0:
            mail = main = matriz[1][c]
        else:
            if matriz[1][c] > mail:
                mail = matriz[1][c]
            if matriz[1][c] < main:
                main = matriz[1][c]
    somat += matriz[l][2]
print('=-'*30)
for l in range (0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-'*30)
print(f'A soma de todos os valores pares digitados é {somap}!')
print(f'A soma da terceira coluna é {somat}!')
print(f'O maior valor da segunda linha é {mail} e o menor é {main}!')
