#Exercício Python 12:
# Faça um algoritmo que leia o preço de um
# produto e mostre seu novo preço, com 5% de
# desconto.

print(f'{'lojas baratao':~^30}')
print('TODA LOJA COM 5% DE DESCONTO')
prod = str(input('qual produto: '))
prec = float(input('Qual preço: '))
desc = prec - (prec * 5/100)
print(f'seu produto {prod} com preço de {prec} , \nsaira por {desc} com 5% de desconto!!')
print('\033[4;35mVote sempre!!\033[m')