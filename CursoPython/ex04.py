#Exercício Python 4:
# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas
# as informações possíveis sobre ele.

STR = str(input('Digite Algo: '))
print(f'o tipo primitivo desse valor é,{type(STR)}')
print(f'''o tipo é :
{'é alfa numerico: ',STR.isalnum()}
\n{'é alfabetico: ',STR.isalpha()}
\n{'é maiusculo',STR.isupper()}
\n{'é minusculo: ',STR.islower()}
\n{'so tem espaço: ',STR.isspace()}
\n{'é numero: ',STR.isnumeric()}
\n{'está capitalizada? ',STR.istitle()}''')