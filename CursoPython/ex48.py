#Exercício Python 48:
# Faça um programa que calcule a soma entre
# todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.
S = 0
Cont = 0
for C in range(1,501,2):
    if C % 3 == 0:
        Cont = Cont +1
        S += C
print(f'A SOMA de todos os {Cont} TOTAL É {S} ',end='')
