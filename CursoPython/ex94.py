#Exercício Python 094: Crie
# um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = {}
cadastro = []
mulheres = []
idacimamedia = []
tot = idade = media = 0

while True:
    dados["nome"] = str(input('Nome: '))
    while True:
        dados["sexo"] = str(input('Sexo: M/F ')).upper() [0]
        if dados["sexo"] in 'MF':
            break
        print('ERR! por favor, digite apenas M ou F. ')

    dados["idade"] = int(input('Idade: '))

    cadastro.append(dados.copy())
    idade += dados["idade"]
    tot += 1
    if dados["sexo"] in 'Ff':
        mulheres.append(dados["nome"])
    while True:
        res = str(input('Quer continuar? S/N ')).upper()[0]
        if res in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if res == 'N':
        break
media = idade/tot
# print(cadastro)
print('-='*40)
print(f' - foram cadastrados {len(cadastro)} pessoas')
print(f' - a Média de idade é {media:.2f}')
print(f' - Lista de mulheres cadastrados {mulheres}')
for p in cadastro:
    if p["sexo"] in 'Ff':
        print(f'{p["nome"]}', end=', ')
print()
print(f' - Pessoas com idade acima da média: ')
for p in cadastro:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')