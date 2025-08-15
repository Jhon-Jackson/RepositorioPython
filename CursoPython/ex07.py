#Exercício Python 7:
# Desenvolva um programa que leia as duas
# notas de um aluno, calcule e mostre a sua
# média.

Nota1 = float(input('Primeira nota: '))
Nota2 = float(input('Segunda nota: '))
media = (Nota1 + Nota2)/ 2
print(f'A media foi {media:2.2f}!')