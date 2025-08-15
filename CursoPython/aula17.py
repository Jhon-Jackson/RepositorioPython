#Nessa aula,
# vamos aprender o que são LISTAS e como
# utilizar listas em Python. As listas são
# variáveis compostas que permitem armazenar
# vários valores em uma mesma estrutura,
# acessíveis por chaves individuais.

#num = [2, 5, 9, 1]
#num[2] = 3
#num.append(7)
#num.sort(reverse=True)
#num.insert(2, 2)
#num.pop() apaga o ultimo ou o valor escollhido
#del num[0]
#if num[5] in num:
#    num.remove(num[5])
#if 2 in num:
#    num.remove(2)
#else:
#    print('não achei o numero ')
#print(num)
#print(f'essa lista tem {len(num)} elementos.')

a = [5,9,3,4,2]
b = a[:]
b[2] = 8
a.insert(0,1)
b.append(10)
#a.sort() and b.sort()
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)
#for cont in range(0,5):
#    valores.append(int(input('Digite um valor: ')))
#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Cheguei ao final da lista.')
