#Exercício Python 082:
# Crie um programa que vai ler vários números
# e colocar em uma lista. Depois disso, crie
# duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados,
# respectivamente.
# Ao final, mostre o conteúdo das três listas
# geradas.

lista = []
listapa = []
listaimp = []
while True:
    n = int(input('Digite um  valor: '))
    lista.append(n)
    r = str(input('Quer continuar? S/N '))
#    pa = n % 2
#    if pa == 0 :
#        listapa.append(n)
#    else:
#        listaimp.append(n)
    if r in 'Nn':
        break
for i, v in enumerate(lista):
    print(i,v)
    if v % 2 == 0 :
        listapa.append(v)
    elif v % 2 == 1:
        listaimp.append(v)
print('#-'*30)
print(f'lista com os valores digitados {sorted(lista)}!')
print(f'lista com numeros pares {sorted(listapa)}!')
print(f'lista com os numeros impares {sorted(listaimp)}!')
print('#-'*30)
