import json
with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\a\biblioteca.json','r', encoding="utf-8") as f:
    #Abre o caminho e vai para o arquivo
    biblioteca = json.load(f)
print(30*'-', "Biblioteca", 30*'-')
def cadastrar():
    global biblioteca
    
    # Pede os dados do livro
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    publicacao = int(input("Digite o ano de publicação: "))

    # Descobre qual será o próximo "TituloN"
    proximo_indice = len(biblioteca) + 1
    chave = f"Livro {proximo_indice}"

    # Monta o livro como dicionário
    livro = {
        "titulo": titulo,
        "Autor": autor,
        "publicacao": publicacao
    }

    # Adiciona ao dicionário principal dentro de uma lista
    biblioteca[chave] = [livro]

    # Salva no JSON (reescreve com 'w')
    with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\a\biblioteca.json', 'w', encoding="utf-8") as f:
        json.dump(biblioteca, f, ensure_ascii=False, indent=4)  

    print(f'Livro cadastrado com sucesso!')

def atualizar():
    global biblioteca
    nome = input("Digite o título do livro que deseja atualizar: ").lower()
    # Após receber o título, faz a substituição
    encontrado = False
    for chave, lista in biblioteca.items():
        for livro in lista:
            if livro["titulo"].lower() == nome:
                #coloque as informações
                novo_titulo = input("Digite o novo título: ")
                novo_autor = input("Digite o novo autor: ")
                nova_publi = int(input("Digite o novo ano de publicação: "))
                #atualiza dentro do json
                livro["titulo"] = novo_titulo
                livro["Autor"] = novo_autor
                livro["publicacao"] = nova_publi

                with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\a\biblioteca.json', 'w', encoding="utf-8") as f:
                    json.dump(biblioteca, f, ensure_ascii=False, indent=4)

                print("Livro atualizado com sucesso!")
                encontrado = True
                break
        if encontrado:
            break

    if not encontrado:
        print("Livro não encontrado.")

def listar():
    global biblioteca
    # Verifica se tem livros cadastrados e os apresenta
    if not biblioteca:
        print("Nenhum livro cadastrado.")
        return
    # printa a lista 
    print("\n--- Lista de Livros ---")
    for chave, lista in biblioteca.items():
        for livro in lista:
            print(f"{chave}: {livro['titulo']}")

def deletar():
    global biblioteca
    nome = input("Digite o título do livro que deseja remover: ").lower()
    encontrado = False

    for chave, lista in list(biblioteca.items()):  # usa list() para evitar RuntimeError ao deletar
        for livro in lista:
            if livro["titulo"].lower() == nome:
                del biblioteca[chave]  # remove o livro do dicionário
                with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\a\biblioteca.json', 'w', encoding="utf-8") as f:
                    json.dump(biblioteca, f, ensure_ascii=False, indent=4)
                print(f'Livro "{nome}" excluído com sucesso!')
                encontrado = True
                break
        if encontrado:
            break

    if not encontrado:
        print("Livro não encontrado.")
    
def sair():
    exit()          
        
        
    
while True:
    #mostra as opções 
    p = [["1 - Cadastrar livros"],
        ["2 - Listar livro"],
        ["3 - Atualizar"],
        ["4 - Remover"],
        ["5 - Sair do sistema"],]
    for i in p:
        print(i)
    opcao = input('Informe a opção desejada: ')
    # Recebe as opções e executa funções
    match opcao:
    
        case '1':
            cadastrar()
        case '2':
            listar()
        case '3':
            atualizar()
        case '4':
            deletar()
        case '5':
            print('Saindo do sistema...')
            sair()
            
            
        
        
    
                






