
print("Bem Vindo(a) ao Sistema do Banco")

def cadastro():
    nome = input("Digite o seu nome: ")
    CPF = input("Digite o seu CPF: ")
    Ano_Nasc = input("Digite o seu ano de nascimento: ")
    Número = input("Digite o seu número de celular: ")
    
    


while True :
    usuario = {}
    print('1 - Cadastrar novo usuario,')
    print('2 - Exibir dados da conta,')
    print('3 - Depositar um valor,')
    print('4 - Sacar um valor,')
    print('5 - Encerrar conta,')
    print('6 - Sair do sistema,')
    opcao = input("Digite qual opção deseja: ")
    if opcao == '1':
        cadastro()
    return 
