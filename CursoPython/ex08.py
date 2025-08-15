#Exercício Python 8:
# Escreva um programa que leia um valor em
# metros e o exiba convertido em centímetros e
# milímetros. km hm dam m dm cm mm

medida = float(input('uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'a medida de {medida}m corresponde a {cm}cm e {mm}mm .')