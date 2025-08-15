#Exercício Python 69:
# Crie um programa que leia a idade e o
# sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
print('-'*25)
print(f'{'CADASTRO DE PESSOAS' :^25}')
print('-'*25)
contid = contsm = contsf = 0
while True:
    Idade = int(input('Qual Sua idade? '))
    if Idade > 18 :
        contid += 1
    Sexo = str(input('Qual seu Sexo? [M/F] ')).strip().upper()[0]
    if Sexo in 'M':
        contsm += 1
    elif Idade < 20 and Sexo in 'F' :
        contsf += 1
    outro = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    if outro in 'N':
        break
print(f'{contid} pessoas maiores que 18 anos')
print(f'{contsm} homens foram cadastrados')
print(f'{contsf} mulheres menores que 20 anos foram cadastrados')