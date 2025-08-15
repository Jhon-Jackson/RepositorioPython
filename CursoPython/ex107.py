# Exercício Python 107:
# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa
# que importe esse módulo e use algumas dessas funções

from uteis.moeda import metade, aumentar, dobro

valor = float(input('Digite o valor: '))
print(f'A metade de {valor} é {metade(valor)}')
print(f'O dobro de {valor} é {dobro(valor)} ')
print(f'aumentando 10%, temos {aumentar(valor,10)}')
