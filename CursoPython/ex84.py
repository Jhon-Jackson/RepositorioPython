#Exercício Python 084:
# Faça um programa que leia nome e peso de
# várias pessoas,guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dado =  []
tot = maip =  menp = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maip = menp = dado[1]
    else:
        if dado[1] > maip:
            maip = dado[1]
        if dado[1] < menp:
            menp = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    tot += 1
    r = str(input('Quer Continuar:[S/N] ?'))
    if r in 'Nn':
        break

print('-*'*30)
print(f'os dados foram: \n{pessoas}')
print(f'foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maip}Kg. Peso  de ' ,end='')
for p in pessoas:
    if p[1] == maip:
        print(f'{p[0]} ',end=',')
print(f'\nO menor peso foi de {menp}Kg. Peso de ',end='')
for p in pessoas:
    if p[1] == menp:
        print(f'{p[0]} ',end=',')
print('\n-*'*30)
