# Exercício Python 097:
# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem
# com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def lin(msg):
    tot = len(msg)
    print('~'* (tot +2))
    print(f'{msg:^{tot+2}}')
    print('~'* (tot + 2))



diga = str(input('Diga qual quer coisa: '))
lin(diga)