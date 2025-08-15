#Exercício Python 62:
# Melhore o DESAFIO 61, perguntando para o
# usuário se ele quer mostrar mais alguns
# termos. O programa encerrará quando ele
# disser que quer mostrar 0 termos.
print('Gerador de termos')
print('-='*10)
Pri = int(input('PRIMEIRO TERMO: '))
Raz = int(input('A RAZAO: '))
termo = Pri
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        print(f'{termo} -> ', end='')
        termo += Raz
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos voice quer mostrar a mais? '))
print(f'acabou com {tot} termos gerados')
