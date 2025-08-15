# Exercício Python 096:
# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
def lin():
    print('-'*40)

def area(a, b):
    aria = a * b
    print(f'A área de um terreno {a}x{b} é de {aria}m²')


lin()
print('Controlhe de Terrenos')
lin()
Larg = float(input('LARGURA (m): '))
Comp = float(input('COMPRIMENTO (m): '))
area(Larg, Comp)
