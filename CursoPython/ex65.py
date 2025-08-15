#Exercício Python 65:
# Crie um programa que leia vários números
# inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e
# qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar
# valores.
print('''CLASSIFICANDO OS NUMEROS
 - DIREI A MEDIA ENTRE OS VALORES
 - MENOR E MAIOR VALOR
 - SOMA DOS VALORES''')
Cont = Num = soma = Media = Maior = Menor = 0
Sair = ' '
while Sair not in 'Nn':
    Num = int(input('DIGITE UM VALOR: '))
    Cont += 1
    soma += Num
    if Cont == 1 :
        Maior = Menor = Num
    else:
        if Num > Maior:
            Maior = Num
        if Num < Menor:
            Menor = Num
    Sair = str(input('Quer continuar[S/N]? ')).upper().strip()[0]# so primeira letra
Media = soma / Cont
print(f'\033[34;0m A Media dos valores é \033[m{Media}! ')
print(f'\033[33;1m O Maior valor digitado foi\033[m {Maior}! ')
print(f'\033[32;4m e o Menor valor digitado foi \033[m{Menor}! ')
print(f' \033[30; A soma de todos os valores é\033[m {soma}! ')
print('acabou')