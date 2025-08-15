# Escreva um programa para aprovar o empréstimo
# bancário para a compra de uma casa. Pergunte o
# valor da casa, o salário do comprador e em quantos
# anos ele vai pagar. A prestação mensal não pode exceder
# 30% do salário ou então o empréstimo será negado.
Casa = float(input('Qual valor da casa? R$: '))
Sal = float(input('Qual seu salario? R$: '))
Par = int(input('Quer pagar em quantos anos? '))
Par1 = Casa/ (Par*12)
print(f'\033[4;33mSe suas parcelas de R$:\033[35m{Par1:.2f}\033[m \033[32mexeder 30% do salario\033[m (\033[35m{Sal*30/100}\033[m),.')
if Par1 >= Sal *30/100:
    print('\033[32mFinaciamento Negado')
else:
    print('\033[4;36mParabens, seu financiamento foi aprovado!!')