#Exercício Python 081:
# Crie um programa que vai ler vários números e
# colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma
# decrescente.
# C) Se o valor 5 foi digitado e está ou não
# na lista.

listanum = list()
cont = contt = 0
while True:
    n = int(input('Digite um Valor: '))
    listanum.append(n)
    #cont += 1
    if n == 5:
        contt += 1
    r = str(input('Deseja continuar? '))
    if r in 'Nn':
        break
listanum.sort(reverse=True)
print(f'os valores digitados foram {(listanum)}.')
print(f'os elementos digitados foram {len(listanum)} vezes!')
if contt == 0 :
    print('O valor 5 nao foi digitado')
else:
    print(f'o valor 5 foi esta na lista  e foi digitado {contt} vezes!')
