from time import sleep, sleep


def lin():
    print('~' * 25)


def contador(i,f,p):
    if p < 0 :
        p *= -1
    if p == 0:
        p = 1
    lin()
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa príncipal
contador(1, 10, 1)
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
