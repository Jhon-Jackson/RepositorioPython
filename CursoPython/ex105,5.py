dado = []
def notas(n, sit=False):
    """
    → Função para analizar notas e situações de varios alunos.
    :param n: uma ou mais notas  dos alunos
    :param sit: valor opcional, indicando se deve ou nao adicionar situação
    :return: dicionario com varias informações sobre a situação da turma.
    """
    Notas = {}
    Notas['Total'] = len(n)
    Notas['maior'] = max(n)
    Notas['menor'] = min(n)
    Notas['Media'] = sum(n)/len(n)
    if sit:
        if Notas['Media'] >=7:
            Notas['situação'] = 'BOA'
        elif Notas['Media'] >= 5:
            Notas['situação'] = 'RAZOAVEL'
        else:
            Notas['situação'] = 'RUIM'
    return Notas


while True:
    n1 = float(input('Digite uma nota: '))
    dado.append(n1)
    while True:
        ress = str(input('Quer continuar? S/N ')).upper().strip()[0]
        if ress in 'SN':
            break
        else:
            print('ERRO!Digite S ou N ')
    if ress == 'N':
        break

resul = notas(dado,sit=True)
print(resul)
help(notas)