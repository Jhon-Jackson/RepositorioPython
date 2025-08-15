#Exercício Python 11:
# Faça um programa que leia a largura e a
# altura de uma parede em metros, calcule a
# sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de
# tinta pinta uma área de 2 metros quadrado

larg = float(input('largura da parade: '))
alt = float(input('altura da parede: '))
area = larg * alt
print(f' sua parede tem a dimensao de {larg} x {alt} e sua area é de {area}m².')
tinta = area / 2
print(f'para pintar essa parede, voce precisara de {tinta}l de tinta ')
