#Nessa aula,
# vamos aprender o que são DICIONÁRIOS e como
# utilizar dicionários em Python.
# Os dicionários são variáveis compostas que
# permitem armazenar vários valores em uma
# mesma estrutura, acessíveis por chaves
# literais.

# dados = dict() ou dados = {}
# pessoas = [{'nome':'Jhon','Sexo':'M','idade': 31}]
# pessoas[0]['peso'] = 85
# print(f'O {pessoas[0]["nome"]} tem {pessoas[0]["idade"]} anos.')
# print(pessoas[0].keys())
# print(pessoas[0].values())
# print(pessoas[0].items())
# for k in pessoas[0].keys():
#     print(k)
# for k, v in pessoas[0].items():
#     print(f'{k} = {v}')

# brasil = []
# estado1 = {'uf':'rio de janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'são paulo','sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(brasil)
# print(estado1)
# print(estado2)

estado = {}
brasil = []
for c in range(0 ,2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'o campo {k} tem o valor {v}')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
