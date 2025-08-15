#Nessa aula, vamos aprender
# o que são LISTAS e como utilizar listas
# em Python. As listas são variáveis compostas
# que permitem armazenar vários valores em uma
# mesma estrutura, acessíveis por chaves
# individuais.

pessoas = [['pedro', 25],['maria',19],['jhon', 31]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

galera = []
dado = []
totmai = totmen = 0
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de  idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de  idade.')
