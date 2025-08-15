#Exercício Python 51:
# Desenvolva um programa que leia o primeiro
# termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa
# progressão.

print('='*30)
print(f'{'10 TERMOS DE UMA PA':^30}')
print('='*30)
P = int(input('Primeiro Termo: '))
R = int(input('A Razao: '))
S = P
for c in range (P,P+10):
    print(f'{S} -->',end='')
    S = S+R
print('ACABOU')
