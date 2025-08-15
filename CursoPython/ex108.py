# Exercício Python 108:
# Adapte o código do desafio #107, criando uma função adicional
# chamada moeda() que consiga mostrar os números como um valor
# monetário formatado.

from uteis.moeda import metade, aumentar, dobro,moeda

valor = float(input('Digite o valor: '))
print(f'A metade de {moeda(valor)} é {(metade(valor,True))}')
print(f'O dobro de {moeda(valor)} é {(dobro(valor,True))} ')
print(f'aumentando 10% temos {(aumentar(valor,10,True))}')