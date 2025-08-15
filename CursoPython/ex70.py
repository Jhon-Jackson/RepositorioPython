#Exercício Python 70:
# Crie um programa que leia o nome e o preço
# de vários produtos. O programa deverá
# perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
print('-='*15)
print(f'{'Lojas e-Fera':-^30}')
print('-='*15)
totp = totmil = cont = menor = 0
prod = ''
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço: '))
    totp += preço
    cont += 1
    if cont == 1:
        menor = preço
        prod = produto
    else:
        if preço < menor and produto:
            menor = preço
            prod = produto
    if preço > 1000:
        totmil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'valor total gasto foi {totp}')
print(f'foram {totmil} produtos acima de R$1.000. ')
print(f'e o produto mais barato foi {prod}, ',end='')
print(f'R${menor}')
print(f'{'OBRIGADO, VOLTE SEMPRE!!':-^40}')