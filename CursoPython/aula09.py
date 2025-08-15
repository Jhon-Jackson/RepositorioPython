#Nessa aula, vamos aprender
# operações com String no Python.
# As principais operações que vamos aprender
# são o Fatiamento de String, Análise com
# len(), count(), find(), transformações com
# replace(), upper(), lower(), capitalize(),
# title(), strip(), junção com join().
frase = 'o Maioral sou eu!'
print('eu'in frase)
print(frase[2::])
print(len(frase))
print(frase.count('a'))
print(frase.find('e'))
print(frase.replace('eu','jhon'))
frase = frase.replace('eu','jhon')
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())#espaços da direita
print(frase.lstrip())#espaços da esquerda
print(frase.split())# faz lista
divido = frase.split()
print(divido[3])
print('-'.join(frase))
