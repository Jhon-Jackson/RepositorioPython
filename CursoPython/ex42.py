#Exercício Python 42:
# Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
print('-='*20)
print('Anaizador de Trianguos')
print('-='*20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos PODEM FORMAR TRIANGURO  ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO ', end='') # lados iguais
    elif r1 != r2 != r3 != r1:
        print('ESCALENO') # todos os aldos diferentes
    #elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
    else:
        print('ISOSCELES') # dois lados iguais, um diferente
else:
    print('os segmentos acima NÃO PODEM FORMAR TRIANGUO')