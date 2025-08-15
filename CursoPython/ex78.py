#Exercício Python 078:
# Faça um programa que leia 5 valores
# numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o
# menor valor digitado e as suas respectivas
# posições na lista.


#num = [int(input('DIGITE OS VALLORES: ')),int(input('DIGITE OS VALLORES: ')),int(input('DIGITE OS VALLORES: ')),
#    int(input('DIGITE OS VALLORES: '))]
#print(num)
#print(f' o numero  maior foi {max(num)} e o numero menor foi {min(num)}')

listaum = []
mai = men = 0
for c in range (0,5):
    listaum.append(int(input(f'Digite um valor na posiçao {c} : ')))
    if c == 0:
        mai = men = listaum[c]
    else:
        if listaum[c] > mai:
            mai = listaum[c]
        if listaum[c] < men:
            men = listaum[c]
print('*=' * 30)
print(f'voce digitou os valores {listaum}')
print(f'o maior valor digitado foi {mai} nas posiçoes!',end='')
for i , v in enumerate(listaum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'o menor valor digitado foi {men}! nas posiçoes!', end='')
for i , v in enumerate(listaum):
    if v == men:
        print(f'{i}...', end='')
print()