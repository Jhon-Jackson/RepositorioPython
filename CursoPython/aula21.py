# Nessa aula,
# vamos continuar nossos estudos de funções em Python,
# aprendendo mais sobre Interactive Help em Python, o uso de
# docstrings para documentar nossas funções, argumentos opcionais
# para dar mais dinamismo em funções Python, escopo de variáveis
# # e retorno de resultados.
# Topicos
# interactive help()
# docstrings
# argumentos  opcionais
# escopo de variaves
# retorno de resultados
         # docstrings - ex : help() print(input__doc__)
def contador(i, f, p):
    """
    →  Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p:passo da contagem
    :return: sem retorno
    """
    cont  = i
    while cont <= f :
        print(f'{c}',end='')
        cont += p
    print('FIM')

help(contador)
        #Argumentos Opcionais ex: def soma(a=0, b=0, c=0,d=0):
                                #     as variaveis recebem valor zero
                                #     se tornam opcionais
def soma(a=0, b=0, c=0,d=0):
    """
    → faz a soma de três valores e mostra o resultado da tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return:  sem retorno
    função criada pelo programador Jhon Jackson
    """
    s = a + b + c + d
    print(f'A soma dos valores {s}')

soma(10,45)

help(soma)

        #escopo de variaveis

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5 #esse valor se perdeu por conta do GLOBAL dentro da def
teste(a)
print(f'A fora vale {a}')

        # retorno de valores - return

def somar1(a=0, b=0, c=0)   :
    s = a + b + c
    return s
print(somar1(3, 4, 5))
S = somar1(3,4,5)
print(S)
r1 = somar1(4,10)
r2 = somar1(6,6)
r3 = somar1(2,1)
print(f'Meus calculos deram {r1}, {r2}, {r3}.')

        # Exercicio ex: return True; return False;

def factorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
print(f'O Fatorial de {n1} é igual a {factorial(n1)}')
f1 = factorial(n1)
f2 = factorial(n2)
f3 = factorial(n3)
print(f'os fatorial de: sao {n1} = {f1}, {n2} = {f2}, {n3} = {f3}.')
