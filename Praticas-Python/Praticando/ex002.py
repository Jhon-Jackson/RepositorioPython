
# file = open("Textos.txt", "r")
# teste = file.read()
# file.close()



# with open("Textos.txt", "a") as file:
#     file.write("\nOlá, Samuel")
#     open("Textos.txt", "r")
#
#
# with open("Textos.txt", "r") as file:
#     teste = file.read()
#     #print(teste)
#
# with open("Textos.txt", "r") as file:
#     for idx, linha in enumerate(file):
#         print(idx, linha.strip())

Arquivo = "Textos.txt"
while True:
    print("para Finalizar Digite Sair")
    nota = input("Escreva uma nota: ")

    with open(Arquivo, "a+", encoding= 'utf-8') as file:
        file.write(nota + "!\n" )

    if nota == "sair":
        linhas = list()
        with open(Arquivo, 'r') as file:
            for linha in file:
                linhas.append(linha)
            linhas.pop(-1)
        break

while True:
    with open(Arquivo, 'w') as file:
        file.writelines(linhas)


    with open(Arquivo, "r") as file :
        for idx, linha in enumerate(file):
            print(f"{idx + 1}. {linha}")

    excluir_linha = int(input("Digito o numero para excluir a linha (0  para sair): ")) - 1
    linhas.pop(excluir_linha)
    if excluir_linha == -1 :
        break
print('Arquivo salvo com as informações: ')
with open(Arquivo, "r") as file :
    for idx, linha in enumerate(file):
        print(f"{idx + 1}. {linha}")
