'''
import os
import json
with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\Aula09/biblioteca.json','r', encoding="utf-8") as f:
#Abre o caminho e vai para o arquivo
    livros = json.load(f)
num_cadastro = 1
print(30*'-', "Biblioteca", 30*'-')
def cadastrar():
    cadastro_liv = input("Digite um ivro para cadastro: ")
    livros[cadastro_liv.lower()]= {'nome': cadastro_liv}
    print(f'Livro {cadastro_liv} cadastrado com sucesso!')

def atualizar():
    livro = input("Digite o nome do livro que deseja atualizar: ").lower()
    if livro in livros():
        try:
            novo_lvr = input("Digite o novo nome: ")
            livros[livro] = novo_lvr
            print(f'Livro "{livro}" atualizado para "{novo_lvr}".')
        except ValueError:
            print("Digite um nome válido.")
    else:
        print("Produto não encontrado.")

def listar():
    livross = input("Digite o livro que deseja listar: ")
    with open (fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\Aula09\biblioteca.json','r', encoding="utf-8") as f:
        if livross in
        
        
            
def ():
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
            livraria()
        case '2':
            listar()
        case '3':
            atualizar()
        case '4':
            deletar()
        case '5':
            sair()
            print('Saindo do sistema...')
            break
              
def sair():
    exit()
'''
    
                
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


'''
 novo_arquivo = input('Informe o nome do arquivo: ').strip().lower()

            if novo_arquivo:
                with open(f'Aula06/{novo_arquivo}.json', 'r', encoding= 'utf-8') as f :1
                    dados_existentes = json.load(f)

            dados_existentes.extend(usuarios)

            with open(f'Aula06/{novo_arquivo}.json', 'w', encoding= 'utf-8') as f :
                json.dump(dados_existentes, f, ensure_ascii=False, indent=4)
            limpar()
            print('Arquivo salvo com sucesso!')
            continue
 --------------------------------------------------------------           
usuario['nome'] = input('Informe o nome: ').strip()
            usuario['idade'] = input(' Informe a idade: ')
            usuario['email'] = input('Digite o email: ').strip().lower()

            usuarios.append(usuario)
            limpar()
            print('Usuário cadastrado com sucesso !')
            continue
'''