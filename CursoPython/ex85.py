#Exercício Python 085:
# Crie um programa onde o usuário possa
# digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados
# os valores pares e ímpares.
# No final, mostre os valores pares e ímpares
# em ordem crescente.
num = [[], []]
n =  0

for c in range (0,5):
    n = int(input(f'Digite {c + 1}°. valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print('=-' * 30)
print(f'Todos os valores: {num}')
print(f'os numeros pares foram {sorted(num[0])}')
print(f'os numeros impares foram {sorted(num[1])}')


