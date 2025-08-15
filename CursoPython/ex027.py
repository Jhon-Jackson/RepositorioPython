#Exercício Python 27:
# Faça um programa que leia o nome completo
# de uma pessoa, mostrando em seguida o
# -primeiro e o último nome separadamente.

n = str(input('Digite seu nome competo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {(nome[0])}')
print(f'Seu utimo nome é {(nome[len(nome)-1])}')
texto = len(nome)
print('seu nome tem',texto,'partes')
