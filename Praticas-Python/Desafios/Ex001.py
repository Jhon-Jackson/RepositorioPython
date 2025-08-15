#1. Escreva um programa para ler um valor do teclado e apresentar o seu antecessor.

def ant (Valor=0):
    Num = Valor - 1
    return Num


num = int(input("Digite um valor: "))
Ant = ant(num)

print(f'O antecessor de {num} é {Ant}!')