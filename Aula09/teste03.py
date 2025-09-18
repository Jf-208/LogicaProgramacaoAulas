livros = {}

def cadastrar():
    cadastro_liv = input("Digite um livro para cadastro: ")
    livros[cadastro_liv.lower()] = {'nome': cadastro_liv}
    print(f'Livro {cadastro_liv} cadastrado com sucesso!')

def atualizar():
    livro = input("Digite o nome do livro que deseja atualizar: ").lower()
    if livro in livros:
        novo_lvr = input("Digite o novo nome: ")
        livros[livro] = {'nome': novo_lvr}
        print(f'Livro "{livro}" atualizado para "{novo_lvr}".')
    else:
        print("Produto não encontrado.")

def listar():
    livross = input("Digite o livro que deseja listar: ").lower()
    if livross in livros:
        print(f'Livro encontrado: {livros[livross]}')
    else:
        print("Livro não encontrado.")

while True:
    p = [
        ["1 - Cadastrar livros"],
        ["2 - Listar livro"],
        ["3 - Atualizar"],
        ["4 - Remover"],
        ["5 - Sair do sistema"],
    ]
    for i in p:
        print(i[0])
    opcao = input('Informe a opção desejada: ')
    match opcao:
        case '1':
            cadastrar()
        case '2':
            listar()
        case '3':
            atualizar()
        case '4':
            print("Função remover ainda não implementada.")
        case '5':
            print("Saindo do sistema...")
            break