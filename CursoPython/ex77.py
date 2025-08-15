#Exercício Python 077:
# Crie um programa que tenha uma tupla com
# várias palavras (não usar acentos). Depois
# disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.

listagem = ('APRENDER', 'programa','linguagem','python',
            'curso','gratis','estudar', 'praticar',
            'trabalhar','mercado','programador','futuro' )
for p in listagem:
    print(f'\nNa palavra {p.upper()} temos', end=' -> ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
