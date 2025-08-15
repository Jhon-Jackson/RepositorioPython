# Exercício Python 113:
# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo
# inválido. Aproveite e crie também uma função leiaFloat()
# com a mesma funcionalidade.

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



Num = leiaInt('Digite um inteiro: ')
NumF = leiaFloat('Digite um Real: ')
print(f'\033[32mo valor inteiro foi {Num} e o real foi {NumF}\033[m')