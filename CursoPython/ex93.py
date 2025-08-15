#Exercício Python 093:
# Crie um programa que gerencie o aproveitamento de um jogador de
# futebol. O programa vai ler o nome do jogador e quantas partidas
# ele jogou. Depois vai ler a quantidade de gols feitos em cada
# partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

dados = dict()
dado = list()
dados["Nome"] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
tot = 0
for c in range(1,partidas +1):
    dado.append(int(input(f'   Quantos gols da partida {c}?')))

dados["Gols"] = dado[:]
dados["total"] = sum(dado)
print('-='*40)
print(dados)
print('-='*40)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*40)
print(f'o jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas.')
for i, v in enumerate(dados["Gols"]):
    print(f'   => Na partida {i +1}º fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
