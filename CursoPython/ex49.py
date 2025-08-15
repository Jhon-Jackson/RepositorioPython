#Exercício Python 49:
# Refaça o DESAFIO 9, mostrando a tabuada de
# um número que o usuário escolher, só que
# agora utilizando um laço for.
from time import sleep
print('-*'*15)
print(f'{('Tabuada inteligente'):^30}')
print('-*'*15)
Num = int(input('DIGA QUAL TABUAR QUER APRENDER: '))
for C in range(1,11):
    print(f'{C} x {Num}, é igual à: \033[4;34m{(C * Num)}\033[m')
    sleep(0.5)
