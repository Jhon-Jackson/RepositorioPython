# Exercício Python 101:
# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import datetime

def voto(num):
    # from datetime import date
    # atual = date.today().year
    # mes = date.today().month
    # hora = date.today().hour
    idade = 0
    ano = datetime.now().year
    idade = ano - num
    if idade >= 18 and idade <= 64:
        # print(f'Com {idade} anos: Voto OBRIGATÓRIO.')
        return f'Com {idade} anos: Voto OBRIGATÓRIO.'
    elif idade >= 16 or idade >= 65:
        # print(f'Com {idade} anos: voto OPCIONAL')
        return f'Com {idade} anos: voto OPCIONAL'
    else:
        # print(f'Com {idade} anos: não Vota.')
        return f'Com {idade} anos: não Vota.'


ID = int(input('Em que ano você nasceu? '))
# voto(ID)
print(voto(ID))
