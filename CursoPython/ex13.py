#Exercício Python 13:
# Faça um algoritmo que leia o salário de um
# funcionário e mostre seu novo salário,
# com 15% de aumento.

Sal = float(input('Salario: '))
aument = Sal + (Sal*15/100)
print(f'parebens vc teve um aumento de 15% , seu novo salario R${aument} . ')
