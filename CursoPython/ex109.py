# Exercício Python 109:
# Modifique as funções que form criadas no desafio 107 para que elas
# aceitem um parâmetro a mais, informando se o valor retornado por
# elas vai ser ou não formatado pela função moeda(), desenvolvida no
# desafio 108.

from uteis.moeda import metade, aumentar, dobro,moeda

valor = float(input('Digite o valor: '))
print(f'A metade de {moeda(valor)} é {(metade(valor,True))}')
print(f'O dobro de {moeda(valor)} é {(dobro(valor,True))} ')
print(f'aumentando 10% temos {(aumentar(valor,10,True))}')