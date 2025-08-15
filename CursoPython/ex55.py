#Exercício Python 55:
# Faça um programa que leia o peso de cinco
# pessoas. No final, mostre qual foi o maior
# o menor peso lidos.
print('-'*30)
print(f'{'COMPARANDO PESO!':^30}')
print('-'*30)
Maior = 0
Menor = 0
for c in range(1,6):
    Peso = float(input(f'Digite O peso da {c}º pessoa: '))
    if c ==1:
        Maior = Peso
        Menor = Peso
    else:
        if Peso > Maior:
            Maior = Peso
        if Peso < Menor:
            Menor = Peso
print(f'O maior Peso foi {Maior}Kg e o menor peso foi {Menor}Kg!!')