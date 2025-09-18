'''
soma = 0       
contador = 0   

while True:
    entrada = input("Digite o salário do funcionário (ou 'fim' para encerrar): ")

    if entrada.lower() == "fim":
        break 

    try:
        salario = float(entrada)
        soma += salario
        contador += 1
    except ValueError:
        print("Valor inválido. Digite um número ou 'fim'.")
        
if contador > 0:
    media = soma / contador
    print(f"\nForam informados {contador} salários.")
    print(f"A média salarial é: R$ {media:.2f}")
else:
    print("Nenhum salário foi informado.")
'''

'''
funcionarios = []  # Lista vazia

while True:
    print("\n--- Menu ---")
    print("1 - Adicionar funcionário")
    print("2 - Remover funcionário")
    print("3 - Listar funcionários")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do funcionário: ")
        funcionarios.append(nome)
        print(f" {nome} foi adicionado à lista.")

    elif opcao == "2":
        nome = input("Digite o nome do funcionário a remover: ")
        if nome in funcionarios:
            funcionarios.remove(nome)
            print(f" {nome} foi removido da lista.")
        else:
            print(" Funcionário não encontrado.")

    elif opcao == "3":
        if len(funcionarios) == 0:
            print(" Nenhum funcionário cadastrado.")
        else:
            print("\n Lista de funcionários:")
            for i, f in enumerate(funcionarios, start=1):
                print(f"{i}. {f}")

    elif opcao == "4":
        print(" Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente!")
'''
'''
senha = input("Digite sua senha: ")

print(f" Sua senha tem {len(senha)} caracteres.")

print(f" Em maiúsculas: {senha.upper()}")


print(f" Em minúsculas: {senha.lower()}")


tem_numero = any(ch.isdigit() for ch in senha)
if tem_numero:
    print(" A senha contém pelo menos um número.")
else:
    print(" A senha NÃO contém números.")
'''
'''
vendas = []

while True:
    entrada = input("Digite o valor da venda (ou 'fim' para encerrar): ")

    if entrada.lower() == "fim":
        break

    try:
        valor = float(entrada)
        vendas.append(valor)
    except ValueError:
        print(" Valor inválido! Digite um número ou 'fim'.")


if len(vendas) > 0:
    maior = max(vendas)           
    menor = min(vendas)           
    total = sum(vendas)           
    media = total / len(vendas)  

    print("\n RESULTADOS DA ANÁLISE ")
    print(f" Maior venda: R$ {maior}")
    print(f" Menor venda: R$ {menor}")
    print(f" Total de vendas: R$ {total}")
    print(f" Média de vendas: R$ {media:.2f}")
else:
    print("Nenhuma venda foi registrada.")
'''
'''
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
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Digite o nome do produto: ").lower()
        if produto in estoque:
            info = estoque[produto]
            print(f" Produto: {produto}")
            print(f" Preço: R$ {info['preco']}")
            print(f" Quantidade: {info['quantidade']}")
        else:
            print(" Produto não encontrado.")

    elif opcao == "2":
        produto = input("Digite o nome do produto: ").lower()
        if produto in estoque:
            try:
                nova_qtd = int(input("Digite a nova quantidade: "))
                estoque[produto]["quantidade"] = nova_qtd
                print(f" Quantidade de {produto} atualizada para {nova_qtd}.")
            except ValueError:
                print(" Digite um número válido.")
        else:
            print(" Produto não encontrado.")

    elif opcao == "3":
        produto = input("Digite o nome do novo produto: ").lower()
        if produto in estoque:
            print(" Produto já existe no estoque.")
        else:
            try:
                preco = float(input("Digite o preço do produto: "))
                qtd = int(input("Digite a quantidade inicial: "))
                estoque[produto] = {"preco": preco, "quantidade": qtd}
                print(f" Produto {produto} adicionado com sucesso!")
            except ValueError:
                print(" Digite valores numéricos válidos para preço e quantidade.")

    elif opcao == "4":
        print("\n Estoque atual:")
        for nome, info in estoque.items():
            print(f"- {nome.capitalize()} | Preço: R$ {info['preco']} | Quantidade: {info['quantidade']}")

    elif opcao == "5":
        print(" Saindo do sistema de estoque...")
        break

    else:
        print("Opção inválida. Tente novamente!")
'''
# Sistema de estoque usando dicionários com keys() e values()
'''
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
'''
# Mini-sistema de RH

funcionarios = []  

while True:
    print("\n--- MENU RH ---")
    print("1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Calcular folha de pagamento")
    print("4 - Relatórios")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
       
        nome = input("Digite o nome do funcionário: ").strip()
        try:
            idade = int(input("Digite a idade: "))
            salario = float(input("Digite o salário: "))
            funcionario = {"nome": nome, "idade": idade, "salario": salario}
            funcionarios.append(funcionario)
            print(f"Funcionário(a) {nome} cadastrado(a) com sucesso!")
        except ValueError:
            print("Digite valores válidos para idade e salário.")

    elif opcao == "2":
      
        if len(funcionarios) == 0:
            print("Nenhum funcionário cadastrado.")
        else:
            print("\nLista de funcionários:")
            for i, f in enumerate(funcionarios, start=1):
                print(f"{i}. Nome: {f['nome']}, Idade: {f['idade']}, Salário: R$ {f['salario']:.2f}")

    elif opcao == "3":
       
        if len(funcionarios) == 0:
            print("Nenhum funcionário cadastrado.")
        else:
            total = sum(f["salario"] for f in funcionarios)
            media = total / len(funcionarios)
            print(f"\nTotal da folha de pagamento: R$ {total:.2f}")
            print(f"Média salarial: R$ {media:.2f}")

    elif opcao == "4":
    
        if len(funcionarios) == 0:
            print("Nenhum funcionário cadastrado.")
        else:
            mais_velho = max(funcionarios, key=lambda x: x["idade"])
            mais_novo = min(funcionarios, key=lambda x: x["idade"])
            mais_caro = max(funcionarios, key=lambda x: x["salario"])
            mais_barato = min(funcionarios, key=lambda x: x["salario"])

            print("\n--- RELATÓRIOS ---")
            print(f"Funcionário mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")
            print(f"Funcionário mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
            print(f"Maior salário: {mais_caro['nome']} (R$ {mais_caro['salario']:.2f})")
            print(f"Menor salário: {mais_barato['nome']} (R$ {mais_barato['salario']:.2f})")

    elif opcao == "5":
        print("Encerrando sistema de RH...")
        break

    else:
        print("Opção inválida. Tente novamente.")
