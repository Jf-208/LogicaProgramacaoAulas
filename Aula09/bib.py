import json
biblioteca = {}
with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\Aula09/biblioteca.json','r', encoding="utf-8") as f:
    #Abre o caminho e vai para o arquivo
    biblioteca = json.load(f)
print(30*'-', "Biblioteca", 30*'-')
def cadastrar():
    global biblioteca
    biblioteca['Livro'] = input("Digite um livro para cadastro: ")
    with open (fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\Aula09/biblioteca.json','w', encoding="utf-8") as f:
        biblioteca =  json.dump(biblioteca, f, ensure_ascii=False, indent=4)
    print(f'Livro cadastrado com sucesso!')

def atualizar():
    nome = input("Digite o nome do livro que deseja atualizar: ").lower()
    if nome in biblioteca:
        novo_lvr = input('Digite o novo nome: ')
        nome[biblioteca] = [novo_lvr]
        with open (fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\Aula09/biblioteca.json','w', encoding="utf-8") as f:
            nome = json.dump(biblioteca, f, ensure_ascii=False, indent=4)
        print('Novo livro registrado com sucesso!')           
    else:
        print("Livro não encontrado.")

def listar():
    global biblioteca
    livross = input("Digite o livro que deseja listar: ")
    with open (fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\Aula09/biblioteca.json','r', encoding="utf-8") as f:
        if livross in biblioteca["livro"]:
            print("Esse livro está listado!")
        else:
            print("o livro não está listado!")

def deletar():
    livro = input("Digite o livro que deseja remover")
    if livro in biblioteca:
        del biblioteca[livro]
        print('livro excluído com sucesso')
def sair():
    exit()          
        
        
    
while True:
    p = [["1 - Cadastrar livros"],
        ["2 - Listar livro"],
        ["3 - Atualizar"],
        ["4 - Remover"],
        ["5 - Sair do sistema"],]
    for i in p:
        print(i)
    opcao = input('Informe a opção desejada: ')
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
            
            
        
        
    
                








