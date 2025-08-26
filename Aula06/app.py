import json 
import os

usuarios = []
novo_arquivo = ''

while True :
    usuario = {}
    print('1 - Cadastrar novo usuario,')
    print('2 - Salvar arquivo JSON,')
    print('3 - Fazer leitura do JSON,')
    print('4 - Sair do sistema,')

    opcao = input ('Informe a opção desejada: ')
    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao:
        case '1':
            usuario['nome'] = input('Informe o nome: ').strip()
            usuario['idade'] = input(' Informe a idade: ')
            usuario['email'] = input('Digite o email: ').strip().lower()

            usuarios.append(usuario)