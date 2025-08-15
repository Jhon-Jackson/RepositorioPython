#Exercício  Python 040:
# Crie um programa que leia duas notas de um aluno
# e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingido
nota1 = float(input('Primeira nota? '))
nota2 = float(input('Segunda nota? '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a media do aluno foi {media}')
if 7> media >= 5:
    print('O aluno está em Recuperação.')
elif media < 5:
    print('O aluno esta reprovado.')
elif media >=7:
    print('O aluno está APROVADO.')