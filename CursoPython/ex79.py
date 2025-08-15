#Exercício Python 079:
# Crie um programa onde o usuário possa
# digitar vários valores numéricos e
# cadastre-os em uma lista.
# Caso o número já exista lá dentro,
# ele não será adicionado.
# No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.

listanum = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('valor adicionado com sucesso')
    else:
        print('\033[31mVALOR já adicionado,tente outro!\033[m')
    SN = str(input('Deseja continuar? S/N : '))
    if SN in 'Nn':
        break
print('=+' * 30)
#listanum.sort()
print(f'voce digitou os valores {sorted(listanum)}')
