#Exercício Python 44:
# Elabore um programa que calcule o valor
# a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
#Nom = 'LOJAS MMSANTOS'
print(f'{'LOJAS MMSANTOS': ^30}')
Pro = float(input('Qual valor do Produto: '))
print('[2]à vista dinheiro/cheque: 10% de desconto')
print('[3]à vista no cartão: 5% de desconto')
print('[4]em até 2x no cartão: preço formal')
print('[5]3x ou mais no cartão: 20% de juros')
Opc = int(input('Escolha opção de Pagamento: '))
if Opc == 2:
    print(f'\033[30mSeu Produto custa {Pro} com a forma de pagamento escolhida custara {Pro - (Pro*10/100)}')
elif Opc == 3:
    print(f'\033[31mSeu Produto custa {Pro} com a forma de pagamento escolhida custara {Pro - (Pro * 5 / 100)}')
elif Opc == 4:
    print(f'\033[32mSeu Produto custa {Pro} com a forma de pagamento escolhida custara 2x de {Pro / 2} ')
elif Opc == 5:
    par = int(input('De quantas vezes quer parcelar?: '))
    print(f'\033[34mSeu Produto custa {Pro} com a forma de pagamento escolhida custara {Pro + (Pro*20/100)} com juros e parcerlas de {par}x de {(Pro + (Pro*20/100))/par}')
else:
    print('\033[33mOpção invalida')