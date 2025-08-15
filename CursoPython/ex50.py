#Exercício Python 50:
# Desenvolva um programa que leia seis números
# inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for
# ímpar, desconsidere-o.
S = 0
for C in range(1,7):
    Num = int(input('DIGITE UM NUMERO: '))
    if Num % 2 == 0:
        S += Num
print(f'A SOMA DOS NUMERO PARES DIGITADOS É {S}')
