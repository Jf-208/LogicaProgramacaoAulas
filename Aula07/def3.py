contas = {}
proximo_numero = 1001

def menu():
    print('1 - Exibir Dados,')
    print('2 - Criar Conta,')
    print('3 - Depositar um valor,')
    print('4 - Sacar um valor,')
    print('5 - Encerrar conta,')
    print('6 - Sair do sistema,') 
    return input("Digite a opção deseja: ")

def exibir_dados():
    if not contas:
        print('Nenhuma conta encontrada!')

    for numero, dados in contas.items():
        print()
        print(f'{20*'-'} Dados Bancários {20*'-'}')
        print(f'Conta: {numero}')
        print(f'Saldo: {dados['saldo']}')
        print(f'Cliente: {dados['nome']} | CPF: {dados['cpf']} | Email: {dados['email']} ')
        print(f'{57*'-'}')
        print()

def criar_conta():
    global proximo_numero
    nome = input('Digite o seu nome: ').strip()
    cpf = input('Digite o seu CPF: ').strip()
    email = input('Digite o seu email: ').strip()
    contas[proximo_numero] = {'nome': nome, 'saldo':0.0, 'cpf':cpf, 'email': email}
    print(f'Conta criada com sucesso! Número da conta: {proximo_numero}')
    proximo_numero +=1
def depositar():
    numero = int(input('Digite o número da conta: ' ))
    if numero in contas:
        valor = float(input("Digite o valor que você deseja depositar: ").replace(',','.'))
        contas[numero]['saldo'] += valor
        print(f'Déposito de R${valor:.2f} realizado com sucesso!')
    else:
        print('Conta não encontrada!')
def sacar():
    numero = int(input('Digite o número da conta: ' ))
    if numero in contas:
        valor = float(input("Digite o valor que você deseja sacar: ").replace(',','.'))
        contas[numero]['saldo'] -= valor
        print(f'Saque {valor:.2f} realizado com sucesso!')
    else:
        print('Conta não encontrada!')
def encerrar_conta():
    numero = int(input('Digite o número da sua conta: '))
    if numero in contas:
        del contas[numero]
        print('Conta excluida com sucesso!')  
    

while True:

    match menu():
        case '1':
            exibir_dados()
        case '2':
            criar_conta()  
        case '3':
            depositar()  
        case '4':
            sacar()  
        case '5':
            encerrar_conta() 
        case '6':
            ("Saindo do Sistema....")
            break
        case _:
            print('Opção invalida.')

