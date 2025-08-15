#Exercício  Python 038:
# Escreva um programa que leia dois números inteiros
# e compare-os. mostrando na tela uma mensagem:
Num1 = int(input('Digite um numero inteiro? '))
Num2 = int(input('Digite outro numero inteiro? '))
if Num1 > Num2:
    print(f'primeiro valor é maior \033[35m{Num1}')
elif Num2 > Num1:
    print(f'segundo valor é maior \033[34m{Num2}')
elif Num1 == Num2:
    print(f'nao a valor maior, os dois sao igual. {Num1} e {Num2}')