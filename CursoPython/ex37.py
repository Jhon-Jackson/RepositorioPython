#Exercício Python 37:
# Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário,
# 2 para octal e 3 para hexadecimal.
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para CONVERSÃO:
[ 1 ] \033[31mCONVERTER PARA BINARIO\033[m
[ 2 ] \033[32mCONVERTER PARA OCTAL\033[m
[ 3 ] \033[33mCONVERTER PARA HEXADECIMAL\033[m''')
opção = int(input('Sua opção: '))
if opção == 1:
     print(f'{num} convertido para binário é igual a {bin(num)[2:]}')
elif opção == 2:
     print(f'{num} convertido para octa é igual a {oct(num)[2:]}')
elif opção == 3:
     print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:
    print('opção invalidade . tente novamente.')