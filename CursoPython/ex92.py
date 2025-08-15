# Exercício Python 092:
# Crie um programa que leia nome, ano de nascimento e carteira de
# trabalho e cadastre-o (com idade) em um dicionário. Se por acaso
# a CTPS for diferente de ZERO, o dicionário receberá também o ano
# de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.

from datetime import datetime
# Obtém a data e hora atuais
agora = datetime.now()
ano = datetime.now().year
# Extrai o ano da data e hora atuais
# ano = agora.year
# Imprime o ano
# print(ano)
# print(agora)
cadastro = dict()
cadastro["Nome"] = str(input('Nome: '))
cadastro["idade"] = int(input('Ano de nascimento: '))
cadastro["CTPS"]  = int(input('Digite Nº da CTPS (0 se nao tem): '))

if cadastro["CTPS"] == 0 :
    print('-=' * 40)
    print(f' - Nome tem valor {cadastro["Nome"]}')
    print(f' - idade tem valor {ano - cadastro["idade"]}')
    print(f' - ctps tem valor {cadastro["CTPS"]}')
    exit()
else:
    cadastro["Contrato"] = int(input('Ano de Contratação: '))
    cadastro["Sal"] = float(input('Salário: R$'))

print('-='*40)
print(f' - Nome tem valor {cadastro["Nome"]}')
print(f' - idade tem valor {ano - cadastro["idade"]}')
print(f' - ctps tem valor {cadastro["CTPS"]}')
print(f' - contratação tem valor {cadastro["Contrato"]}')
print(f' - Salário tem valor {cadastro["Sal"]}')
print(f' - aposentadoria tem valor {(ano - cadastro["idade"])+35}')
