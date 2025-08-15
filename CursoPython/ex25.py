#Exercício Python 25:
# Crie um programa que leia o nome de uma
# pessoa e diga se ela tem “SILVA” no nome.
from time import sleep
nome = str(input('DIGITE SEU NOME COMPLETO: ')).strip().upper()
separa = nome.split()
print(nome)
print('anaizando nome ...')
sleep(1)
print('SILVA' in nome)
