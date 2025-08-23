# 3. Escreva um programa para ler o número total de eleitores de um município, o
# numero de votos brancos, nulos e válidos. Apresente a percentagem que cada
# um representa, em relação ao total de eleitores.


def porcentage(Total, fraçao):
    porcento = (fraçao / Total) * 100
    return porcento



print('-*'*20)
print(f'{'Eleição Eleitoral de Maceio':^40}')
print('*-'*20)

print("Contagem de Votos")
nulos = int(input('Quantos Votos nulos?: '))
branco = int(input('Quantos Votos em Branco?: '))
valido = int(input('Quantos Votos Válidos?: '))

soma = nulos + branco + valido
fraçao = float(soma)
print(f'Total de Eleitores,\n {fraçao:,.1f} Eleitores votaram!')

print(f'{porcentage(soma, nulos):.1f}% Votaram Nulo!')
print(f'{porcentage(soma, branco):.1f}% Votaram em Branco!')
print(f'{porcentage(soma, valido):.1f}% tiveram Os Votos Validos!')