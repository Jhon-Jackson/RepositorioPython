# Exercício Python 090:
# Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura
# na tela.

# lista  =  list()
# dados = dict()
# for c in range(0,1):
#     dados['nome'] = str(input('Nome: '))
#     dados['Media'] = float(input(f'Media de {dados["nome"]}: '))
#     # lista.append(dados.copy())
#     if dados["Media"] < 5 :
#         reprov = 'Recuperação'
#     else:
#         reprov = 'Aprovado'
# print(dados)
# print('-=' * 30)
# print(f'- nome é igual a {dados["nome"]}')
# print(f'- média é igual a {dados["Media"]}')
# print(f'situação é igual a {reprov}')

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'média de {aluno["nome"]}: '))
if aluno['media'] >=7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] >=7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' *30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
