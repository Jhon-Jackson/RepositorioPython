#Exercício Python 54:
# Crie um programa que leia o ano de
# nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

from datetime import date
ano = date.today().year
cont = 0
contt = 0

for c in range(1,6):
    idade = int(input(f'Em que ano {c}º pessoa  nasceu?: '))
    anos = ano - idade
    if anos >= 21 :
        cont += 1
    else:
        contt += 1
print(f' {cont} sao maiores de idade e {contt} ainda nao sao maior de idade')