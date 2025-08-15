def leiadinheiro(msg):
    ok = False
    while not ok:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[31mErro! \"{n}\" é um preço inválido.\033[m')
        else:
            ok = True
            return float(n)


def leiaInt(msg):
    ok = False
    Valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            Valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return Valor
