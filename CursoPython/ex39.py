from datetime import date
#Exercício  Python 39: Faça um programa
# que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que
# falta ou que passou do prazo.
print('=+'*15)
print('Esta na hora de se alista!!')
print('=+'*15)
Atual = date.today().year
Ano = int(input('Digite o ano que nasceu? '))
Id = Atual - Ano
if Id == 18:
    print(f'voce esta na idade de se alistar, sua idade \033[32m {Id}')
elif Id < 18 :
    print(f'vc ainda nao esta na idade ({Id} Anos) de se alistar porem faltam \033[36m{18-Id}\033[m anos')
else:
    print(f' ja passou o tempo de se alistar ({Id} Anos) e vc estar atraso \033[37m{Id-18}\033[m anos')