#Exercício Python 56:
# Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo, qual é o nome do
# homem mais velho e quantas mulheres
# têm menos de 20 anos.

somaid = 0
mediaid = 0
maiorid = 0
nomevel = ''
totm = 0
nom = ''
nom1 = ''
for p in range(1,5):
    print(f'_________[{p}]º PESSOA________')
    nome = str(input('Qual seu nome: '))
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo[M/F]: ')).strip().upper()
    somaid += idade
    if p == 1 and sexo in 'Mm':
        maiorid = idade
        nomevel = nome
    if sexo in 'Mm' and idade > maiorid:
        maiorid = idade
        nomevel = nome
    if sexo in 'Ff' and idade < 20:
        totm += 1
        nom = nome
        if totm >= 2:
            nom1 = nome

mediaid = somaid /4
print(f'A media de idade do grupo é de {mediaid:.2f} anos.')
print(f' O homen mais velho tem {maiorid} anos e se chama {nomevel}..')
print(f'ao todo sao {totm} mulheres com menos de 20 anos e se chama {nom} e {nom1}!')