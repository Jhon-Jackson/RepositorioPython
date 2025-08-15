#Exercício Python 64:
# Crie um programa que leia vários números
# inteiros pelo teclado.
# O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de
# parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre
# eles (desconsiderando o flag).
print('+'*30)
print('contador de numeros')
print('+'*30)
cont = soma = Num = Soma = 0
#cont = 0
#soma = 0
#Num = 0
#Soma = 0
Num = int(input('DIGITE QUAL QUER VALOR INTEIRO OU 999 PARA ENCERRAR: '))
while Num != 999:
    #Num = int(input('DIGITE QUAL QUER VALOR INTEIRO OU 999 PARA ENCERRAR: '))
    soma += Num
    #Soma = soma - 999
    cont += 1
    Num = int(input('DIGITE QUAL QUER VALOR INTEIRO OU 999 PARA ENCERRAR: '))
#print(f'voce digitou {cont - 1} valores e a soma de todos eles é {Soma}')
print(f'voce digitou {cont} valores e a soma de todos eles é {soma}')
