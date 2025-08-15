#Exercício Python 095:
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento
# de cada jogador.

dados = dict()
dado = list()
Todosdados = []
while True:
    dados["Nome"] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    tot = 0

    for c in range(1,partidas +1):
        dado.append(int(input(f'   Quantos gols da partida {c}?')))

    dados["Gols"] = dado[:]
    dados["total"] = sum(dado)
    Todosdados.append(dados.copy())
    dado.clear()
    while True:
        res = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
        if res in "SN":
            break
        print('ERRO! Responda S ou N')
    if res == 'N':
        break
print('-=' * 40)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print('-=' * 40)
for k, v in enumerate(Todosdados):
    print(f'{k:>3}',end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(Todosdados):
        print(f'ERRO! Não existe jogador com codígo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {Todosdados[busca]["Nome"]}: ')
        for i, g in enumerate(Todosdados[busca]['Gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('-' *40)
print('<< VOLTE SEMPRE >>')
