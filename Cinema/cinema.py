'''
print(40*"_", "Bem-Vindo ao Cinema 2º DS", 40*"-")
nome = input("Digite o seu nome: ").upper()
idade = int(input("Digite sua idade: "))

sala01 = "Homem-Aranha (10 anos)"
sala02 = "1917 (14 anos)"   
sala03 = "Interestelar (10 anos)"
sala04 = "Cidade de Deus (16 anos)"
sala05 = "Pulp Fiction (18 anos)"

print("As salas disponíveis para a sua idade são: ")
while True :
    print("1 - Homem-Aranha (10 anos)")
    print("2 - 1917 (14 anos)")
    print("3 - Interestelar (10 anos)")
    print("4 - Cidade de Deus (16 anos)")
    print("5 - Pulp Fiction (18 anos)")
    print("6 - Sair")
    opcao = input("Escolha um filme: ")
    if opcao == "1":
        print(f"{nome}, você escolheu assistir {sala01}.")
    
        break
    elif idade >= 16:
        print("Você está autorizado a assistir os seguintes filmes: ")
        print("1 - Homem-Aranha (10 anos)")
        print("2 - 1917 (14 anos)")
        print("3 - Interestelar (10 anos)")
        print("4 - Cidade de Deus (16 anos)")
        break
    elif idade >= 14:
        print("Você está autorizado a assistir os seguintes filmes: ")
        print("1 - Homem-Aranha (10 anos)")
        print("2 - 1917 (14 anos)")
        print("3 - Interestelar (10 anos)")
        break
    elif idade >= 10:
        print("Você está autorizado a assistir os seguintes filmes: ")
        print("1 - Homem-Aranha (10 anos)")
        print("3 - Interestelar (10 anos)")
        break
    elif idade < 10:
        print("Você não está autorizado a assistir nenhum filme.")
        break
    else:
        print("Opção inválida. Tente novamente.")
        continue    
'''

sala01 = "Homem-Aranha"
min1 = 10
sala02 = "1917"  
min2 = 14
sala03 = "Interestelar"   
min3 = 10
sala04 = "Cidade de Deus"
min4 = 16
sala05 = "Pulp Fiction"
min5 = 18   

while True:
    print(40*"_", "Bem-Vindo ao Cinema 2º DS", 40*"-")
    print("Escolha uma opcão do filme que deseja assistir: ")
    print(f'1. Sala 01 - {sala01}: Idade minima {min1} anos')
    print(f'2. Sala 02 - {sala02}: Idade minima {min2} anos')
    print(f'3. Sala 03 - {sala03}: Idade minima {min3} anos')
    print(f'4. Sala 04 - {sala04}: Idade minima {min4} anos')
    print(f'5. Sala 05 - {sala05}: Idade minima {min5} anos')
    print("6. Sair")
    opcao = int(input("Digite a opção desejada: "))
    idade = input("Digite sua idade: ")
    if opcao == 1:
        if idade >= min1:
            print("Bem vindo ao Cinema 2º DS")
            print(f"Ingresso para: ({sala01})")
            print(f"Sala: 01")
            break
        else:
         print("Desculpe, você não tem idade suficiente para assistir a este filme.")
    elif opcao == 2:
        if idade >= min2:
            print("Bem vindo ao Cinema 2º DS")
            print(f"Ingresso para: ({sala02})")
            print(f"Sala: 02")
            break
        else:
         print("Desculpe, você não tem idade suficiente para assistir a este filme.")
    elif opcao == 3:
        if idade >= min3:
            print("Bem vindo ao Cinema 2º DS")
            print(f"Ingresso para: ({sala03})")
            print(f"Sala: 03")
            break
        else:
         print("Desculpe, você não tem idade suficiente para assistir a este filme.")
    elif opcao == 4:
        if idade >= min4:
            print("Bem vindo ao Cinema 2º DS")
            print(f"Ingresso para: ({sala04})")
            print(f"Sala: 04")
            break
        else:
         print("Desculpe, você não tem idade suficiente para assistir a este filme.")
    elif opcao == 5:
        if idade >= min5:
            print("Bem vindo ao Cinema 2º DS")
            print(f"Ingresso para: ({sala05})")
            print(f"Sala: 05")
            break
        else:
         print("Desculpe, você não tem idade suficiente para assistir a este filme.")
    elif opcao == 6:
         print("Saindo do sistema!")
         break
    else:
            print("Opção inválida. Tente novamente.")