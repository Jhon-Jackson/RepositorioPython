#Exercício Python 089:
# Crie um programa que leia nome e duas notas
# de vários alunos e guarde tudo em uma lista
# composta. No final, mostre um boletim
# contendo a média de cada um e permita que
# o usuário possa mostrar as notas de cada
# aluno individualmente.

turma = list()
aluno = list()
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    turma.append(aluno[:])
    aluno.clear()
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
#print(turma)
print('No.   NOME       MÉDIA')
print('-'*30)
for c in range(len(turma)):
    print(f'{c}  {turma[c][0] :<10}     {(turma[c][1] + turma[c][2])/2 :>4}')
print('-'*30)
while True:
    m = int((input('Mostrar notas de qual aluno? (999 interrompe) ')))
    if m < 999:
        print(f'Notas de {turma[m][0]} são [{turma[m][1]}, {turma[m][2]}]')
    if m == 999:
        print('FINALIZANDO')
        break
    print('-'* 30)
print('-'* 30)
print('acabou, volte sempre!')
