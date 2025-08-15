#Exercício Python 66:
# Crie um programa que leia números inteiros
# pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999,
# que é a condição de parada. No final,
# mostre quantos números foram digitados e
# qual foi a soma entre elas
# (desconsiderando o flag.
s = cont = 0
while True :
    n = int(input('digite um numero: '))
    if n == 999:
        break
    cont+=1
    s+=n
if s >= 10 and s <= 40:
    s = (f'\033[33m{s}\033[m')
print(f' DIGITOU {cont} valores e a SOMA DOS VALORES É {s}', end=' ')
print('acabou')