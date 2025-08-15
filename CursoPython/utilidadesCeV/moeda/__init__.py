from operator import indexOf


def aumentar(V=0, P=0,formato=False):
    res = V + (V * P/100)
    return res if formato is False else moeda(res)


def diminuir(V=0, P=0,formato=False):
    res = V - (V * P/100)
    return res if formato is False else moeda(res)


def dobro(V,formato=False):
    res = V * 2
    return res if not formato else moeda(res)


def metade(V,formato=False):
    res = V / 2
    return res if not formato else moeda(res)


def moeda(n):
    forma = (f'R${n:.2f}').replace('.',',')
    return forma


def resumo(P=0, PA=0,PD=0):
    """
    função para resumir moeda com implementaçoes de outras funções
    como: aumentar, diminuir, dobro e metade do valor.
    :param P: recebe preço(valor)
    :param PA: recebe a porcentagem para aumentar
    :param PD: recebe a porcentagem para diminuir
    :return: n/d
    """
    print('-'*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-'*35)
    print(f'Preço analisado: \t{moeda(P)}')
    print(f'Dobro do preço:  \t{dobro(P,True)}')
    print(f'Metade do preço: \t{metade(P, True)}')
    print(f'{PA}% de aumento:  \t{aumentar(P,PA,True)}')
    print(f'{PD}% de redução:  \t{diminuir(P,PD,True)}')
    print('-' * 35)


def leiaInt(msg):
    ok = False

    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um Numero Valido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mentrada de dados  interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):

    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um Numero Real Valido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mentrada de dados  interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


