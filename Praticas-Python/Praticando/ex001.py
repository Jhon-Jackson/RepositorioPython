
total_lista = []

def mostrar_menu():
    print("\n Opções")
    print("1. Mostrar Tarefas")
    print("2. Adc Tarefas")
    print("3. Remover Tarefas")
    print("4. Sair")

def Visualiar_Tarefas():
    if not total_lista:
        print("Lista sem Tarefas")
    else:
        print("\nSuas Tarefas")
        for idx, task in enumerate(total_lista, start=1):
            print(f"{idx}. {task}")

def adc_task():
    task = input("Digite sua tarefa: ")
    total_lista.append(task)
    print("Tarefa adicionada!")

def remover_task():
    Visualiar_Tarefas()
    try:
        index = int(input("Digite numero referente a tarefa para remover: ")) - 1
        removido = total_lista.pop(index)
        print(f"Excluido: {removido}")
    except (ValueError, IndexError):
        print("Invalid task number")


while True:
    mostrar_menu()
    escolher = input("Escolha uma opção (1-4): ")

    if escolher == "1":
        Visualiar_Tarefas()
    elif escolher == "2":
        adc_task()
    elif escolher == "3":
        remover_task()
    elif escolher == "4":
        print("Até Mais!")
        break
    else:
        print("Opção Invalida, por favor escolha de 1-4.")

        