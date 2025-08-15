#Nessa aula,
# vamos começar nossos estudos com os laços
# e vamos fazer primeiro o “for”, que é uma
# estrutura versátil e simples de entender.
# Por exemplo:
# for c in range(0, 4):
# print(c)
# print(‘Acabou’)
from time import sleep
#for c in range (1,3):
#    print('oi')
#    sleep(1)
#    for d in range (1):
#        nom = str(input('Diga seu nome: '))
#        sleep(0.5)
#print('FIM')
#print(nom)
i = int(input('INICIO '))
f = int(input('Fim '))
p = int(input('Passo '))
s = 0
for c in range(i,f+1, p):
    print(c)
    s += c
print(f'o total das soma é {s}')