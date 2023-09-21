# Inicializar uma lista vazia para a lista de compras
lista_de_compras = []

while True:
    print("Escolha uma opção:")
    print("1. Adicionar item")
    print("2. Apagar item")
    print("3. Listar itens")
    print("4. Sair")
    
    opcao = input("Digite o número da opção: ")
    
    if opcao == "1":
        item = input("Digite o item que deseja adicionar à lista: ")
        lista_de_compras.append(item)
        print(f"'{item}' foi adicionado à lista de compras.")
    elif opcao == "2":
        if lista_de_compras:
            print("\nItens na lista de compras:")
            for i, item in enumerate(lista_de_compras, start=1):
                print(f"{i}. {item}")
            indice = int(input("\nDigite o número do item que deseja apagar: "))
            if 1 <= indice <= len(lista_de_compras):
                item_removido = lista_de_compras.pop(indice - 1)
                print(f"'{item_removido}' foi removido da lista de compras.")
            else:
                print("Índice inválido. Tente novamente.")
        else:
            print("A lista de compras está vazia.")
    elif opcao == "3":
        if lista_de_compras:
            print("\nItens na lista de compras:")
            for i, item in enumerate(lista_de_compras, start=1):
                print(f"{i}. {item}")
        else:
            print("A lista de compras está vazia.")
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
