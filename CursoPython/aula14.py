#Nessa aula, vamos continuar
# a estudar os laços e vamos aprender
# a usar a estrutura de repetição while
# no Python. Por exemplo:
#0c=1 while c !=10:
#print(c)
#c+=1
#print(‘Acabou’)
from time import sleep
c=1
while c!=10+1:
    print(f'\033[33m{c}\033[m', end='\033[32m,\033[m')
    c+=1
    sleep(0.5)
print(f'\n\033[34m{'Acabou'}')