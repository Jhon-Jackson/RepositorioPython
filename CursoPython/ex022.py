#Exercício Python 22:
# Crie um programa que leia o nome
# de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas
# e minúsculas.
#– Quantas letras ao todo
# (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
from random import randint
frase = ('curso em video pytho')
dividido = frase.split()
dividido.append('jhon')
print(dividido)
print(len(dividido))
aleat = randint(0,len(dividido)-1)
print(aleat)
print(f'{(dividido[aleat])}')
#parte = len(dividido)
#print(parte)
#nome = str(input('Digite seu nome completo: ')).strip()
#print(f'analisando seu nome ... {nome}')
#print(f'seu nome em maiusculo é {nome.upper()}')
#print(f'seu nome em minuscuo é {nome.lower()}')
#print(f'seu nome tem ao todo {len(nome)-(nome.count(' '))} letras.')
#print(f'seu primeiro nome tem {nome.find(' ')} letras.')
#separa = nome.split()
#print(f'seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
