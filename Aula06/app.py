import json 
import os
#Base do codigo
usuarios = []
novo_arquivo = ''
#Variaveis 

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

while True :
    usuario = {}
    print('1 - Cadastrar novo usuario,')
    print('2 - Salvar arquivo JSON,')
    print('3 - Fazer leitura do JSON,')
    print('4 - Sair do sistema,')
    #Comandos que a gente seleciona 

    opcao = input ('Informe a opção desejada: ')
    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao:
        case '1':
            usuario['nome'] = input('Informe o nome: ').strip()
            usuario['idade'] = input(' Informe a idade: ')
            usuario['email'] = input('Digite o email: ').strip().lower()

            usuarios.append(usuario)
            limpar()
            print('Usuário cadastrado com sucesso !')
            continue
        case '2':
            novo_arquivo = input('Informe o nome do arquivo: ').strip().lower()

            if novo_arquivo:
                with open(f'Aula06/{novo_arquivo}.json', 'r', encoding= 'utf-8') as f :
                    dados_existentes = json.load(f)

            dados_existentes.extend(usuarios)

            with open(f'Aula06/{novo_arquivo}.json', 'w', encoding= 'utf-8') as f :
                json.dump(dados_existentes, f, ensure_ascii=False, indent=4)
            limpar()
            print('Arquivo salvo com sucesso!')
            continue

        case '3':
            if not novo_arquivo:
                novo_arquivo = input('Digite o nome do arquivo: ').strip().lower()
            with open(f'Aula06/{novo_arquivo}.json', 'r', encoding= 'utf-8') as f:
                dados = json.load(f)
            print(f'{'-'*20} USUARIOS {'-'*20}\n')
            for usuario in dados:
                for chave in usuario:
                    print(f'{chave.capitalize()}: {usuario.get(chave)}')
                print('-'*40)
            continue
        case '4':
            print('Saindo do sistema! ')
            break
        case _:
            print('Opção invalida.')
            continue

                                                       
                                 