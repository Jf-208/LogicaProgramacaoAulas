estoque = {
    "arroz": {"preco": 20.0, "quantidade": 50},
    "feijao": {"preco": 8.5, "quantidade": 30},
    "macarrao": {"preco": 5.0, "quantidade": 100}
}

while True:
    print("\n--- MENU DE ESTOQUE ---")
    print("1 - Consultar produto")
    print("2 - Atualizar quantidade")
    print("3 - Adicionar novo produto")
    print("4 - Listar estoque")
    print("5 - Remover produto")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Digite o nome do produto: ").lower()
        if produto in estoque.keys():
            info = estoque[produto]
            print(f"Produto: {produto.capitalize()}")
            print(f"Preço: R$ {info['preco']}")
            print(f"Quantidade: {info['quantidade']}")
        else:
            print("Produto não encontrado.")

    elif opcao == "2":
        produto = input("Digite o nome do produto: ").lower()
        if produto in estoque.keys():
            try:
                nova_qtd = int(input("Digite a nova quantidade: "))
                estoque[produto]["quantidade"] = nova_qtd
                print(f"Quantidade de {produto} atualizada para {nova_qtd}.")
            except ValueError:
                print("Digite um número válido.")
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        produto = input("Digite o nome do novo produto: ").lower()
        if produto in estoque.keys():
            print("Produto já existe no estoque.")
        else:
            try:
                preco = float(input("Digite o preço do produto: "))
                qtd = int(input("Digite a quantidade inicial: "))
                estoque[produto] = {"preco": preco, "quantidade": qtd}
                print(f"Produto {produto} adicionado com sucesso!")
            except ValueError:
                print("Digite valores numéricos válidos para preço e quantidade.")

    elif opcao == "4":
        print("\nEstoque atual:")
        for nome in estoque.keys():  
            info = estoque[nome]
            print(f"{nome.capitalize()} | Preço: R$ {info['preco']} | Quantidade: {info['quantidade']}")

        print("\nValores do estoque (values):")
        for info in estoque.values():  
            print(info)

    elif opcao == "5":
        produto = input("Digite o nome do produto a remover: ").lower()
        if produto in estoque.keys():
            estoque.pop(produto)  
            print(f"Produto {produto} removido do estoque.")
        else:
            print("Produto não encontrado.")

    elif opcao == "6":
        print("Saindo do sistema de estoque...")
        break

    else:
        print("Opção inválida. Tente novamente!")