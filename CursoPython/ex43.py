#Exercício Python 43:
# Desenvolva uma lógica que leia o peso e a
# altura de uma pessoa, calcule seu Índice
# de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
print('=-='*15)
print('CALCULANDO IMC')
print('=-='*15)
Peso = float(input('Qual seu Peso: '))
Alt = float(input('Qual sua altura: '))
IMC = Peso / (Alt * Alt)
print(f'Seu peso {Peso} e sua altura {Alt} tem como IMC {IMC:.2f}')
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC >= 18.5 and IMC <=25:
    print('Peso Ideal')
elif IMC >= 25 and IMC <=30:
    print('Sobrepeso')
elif IMC >= 30 and IMC <=40:
    print('Obesidade')
else:
    print('Obesidade Morbida')
