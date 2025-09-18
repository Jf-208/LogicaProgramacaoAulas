import json
with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\Aula09\teste.json','r', encoding="utf-8") as f:
#Abre o caminho e vai para o arquivo
    livros = json.load(f)
def cadastrar():
    global livros
    cadastro = input("Digite um livro para cadastro: ")
    livros[cadastro.lower()]= {'nome': cadastro}
    print(f'Livro {cadastro} cadastrado com sucesso!')
    with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\Aula09\teste.json' , 'w', encoding= 'utf-8') as s:
        s.write(f'{cadastro}')
def sair():
    exit()


while True:
    opcao = input("Digite uma opção: ")
    match opcao:
        case "1":
            cadastrar()
        case "2":
            sair()