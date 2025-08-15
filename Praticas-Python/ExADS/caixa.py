# Nome: Jhon Jackson da Silva Santos
# Curso: Análise e Desenvolvimento de Sistemas
# Disciplina: Projeto Integrador Extensionista – ADS 1
# Semestre Letivo: 1º Termo – 2025


Produtos = {}
Itens = []
tot = 0
print('-*' * 30)
print(f'{'Mercado LeveMais PaquePouco':^50}')
print('-*'*30)
while True:
    n = 1
    # trecho para fazer loop dos produtos e preços
    try:
        while True:
            Produtos["item"] = str(input(f'Produto {n}: '))
            while True:
                Produtos["preço"] = float(input(f'Preço {n}: '))
                if Produtos["preço"] <=0 :
                    print('Preço invalido, tente novamente')
                else:
                    break
            n += 1
            tot += Produtos["preço"]
            Itens.append(Produtos.copy())
            if Produtos["preço"] <= 0 :
                print('Preço invalidado, Tente novamente!')
                continue
            msg = int(input("Para encerrar Digite [0] Continuar [1] : "))
            if msg == 0:
                break

    except:
        print('Tente novamente!')
        continue
# Programa apresentável com as informações da compra.
    print('-*' * 30)
    print(f'{'Mercado LeveMais PaquePouco':^50}')
    print('-*'*30)
    for c, v in enumerate(Itens):
        print(f'{v["item"]:<10}: $R{v["preço"]:<10.2f}')
    #parte final com pagamento e troco.
    print(f'Total à pagar: {tot:.2f}')
    Pag = float(input('Pagamento em Dinheiro: '))
    Troco = (f'{Pag - tot:.2f}')
    print(f'Pagamento:R$ {Pag}')
    print(f'Troco:R$ {Troco}')
    print("Obrigado , Volte sempre!")
