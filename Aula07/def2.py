
def menu():
    print('1 - Cadastrar novo usuario,')
    print('2 - Exibir dados da conta,')
    print('3 - Depositar um valor,')
    print('4 - Sacar um valor,')
    print('5 - Encerrar conta,')
    print('6 - Sair do sistema,')
    input('Informe a opção desejada: ')
def cadastro():
    nome = input("Digite o seu nome: ")
    CPF = input("Digite o seu CPF: ")
    Ano_nasc = input("Digite o seu ano de nascimento: ")
    Número = input("Digite o seu número de celular: ")
def dados():
    print("Conta: ")
    print("Dados: ")
    print("Deposito: ")
    print("Saque: ")   
def deposito():
    ...
def saque():
    ...
def excluir_conta():
    ...

while True:

    match menu():
        case '1':
            cadastro()
        case '2':
            dados()  
        case '3':
            deposito()  
        case '4':
            saque()  
        case '5':
            excluir_conta() 
        case '6':
            ("Saindo do Sistema....")
            break
        case _:
            print('Opção invalida.')

    
