#Exercício Python 72:
# Crie um programa que tenha uma dupla
# totalmente preenchida com uma contagem
# por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo
# teclado (entre 0 e 20) e mostrá-lo por
# extenso.

cont = ('zero','um','dois','tres','quatro',
        'cinco','seis','sete','oito','nove',
        'dez','onze','doze','treze','catorze',
        'quinze','dezesseis','dezessete','dezoito',
        'dezenove','vinte')
while True:
        while True:
                num = int(input('Digite um numero entre 0 e 20: '))
                if 0 <= num <= 20:
                        break
                print('Tente novamente. ', end='')
        print(f'voce digitou o numero {cont[num]}')
        quer = str(input('quer continuar? S/N ')).upper().strip()
        if quer == 'N':
                break
print('Fim do Programa!')