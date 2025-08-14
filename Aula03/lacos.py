'''

Problema: Crie um sistema que calcule o indice de massa corporal(IMC)
do usuario, mostre o valor do IMC na tela, e retorne se o usuario 
estiver no peso ideal ou se precisar emagrecer ou engordar mais. 
Utilize a tabela do IMC para definir os valores.

imc = peso/ (altura * altura)
'''
'''
print(40*"_",'Calculadora de IMC',40*'-')
nome = str(input('Digite o seu nome:'))
peso = float(input('Digite seu peso: ').replace(',','.'))
altura = float(input('Digite sua altura:').replace(',','.'))

imc = peso / (altura * altura)
print()
print(f'Seu IMC é:{imc:.2f}')

if imc <= 18.5:
    print(nome,',Seu Peso está Abaixo do normal')
elif imc <= 24.9:
    print(nome,',Seu Peso está Normal')
elif imc <= 29.9:
    print(nome,',Você Está Sobrepeso')
elif imc <= 34.9:
    print(nome,',Você Está Com Obesidade Grau I')
elif imc <= 39.9:
    print(nome,',Você Está Com Obesidade Grau II')
else:
    print(nome,',Você Está Com Obesidade Grau III')
'''
'''
Problema 2: Um elevador de carga possui capacidade para 200kg.
Crie um programa que receba do usuario seu peso e o peso da carga
e verifica se a carga está autorizada a usar o elevador ou não.
'''
'''
print(40*"-",'Elevador',40*'-')
nome = str(input('Digite o seu nome:'))
peso = float(input('Digite seu peso: ').replace(',','.'))
peso_carga = float(input('Digite o peso de sua carga: ').replace(',','.'))
capac_total = peso + peso_carga

if capac_total <= 200:
    print('O Limite de Carga é 200KG')
    print('Seu peso total e:',capac_total)
    print(nome,'Sua carga não excede o limite, você está autorizado a utilizar o elevador')
elif capac_total > 200:
    print('O Limite de Carga é 200KG')
    print('Seu peso total e:',capac_total)
    print(nome,'Sua carga excede o limite, sem autorização para utilizar o elevador')
'''
'''
cont = 0
while cont < 15:
    cont  += 1
    if cont % 2 == 0:
        print(cont) 
    elif cont >= 7:
        break
    else: 
        continue 

print("Contando...")
'''
'''
print(40*"_",'Calculadora de IMC',40*'-')
while True:
    nome = str(input('Digite o seu nome:'))
    peso = float(input('Digite seu peso: ').replace(',','.'))
    altura = float(input('Digite sua altura:').replace(',','.'))

    imc = peso / (altura * altura)
    print()
    print(f'Seu IMC é:{imc:.2f}')

    if imc <= 18.5:
        print(nome,',Seu Peso está Abaixo do normal')
    elif imc <= 24.9:
        print(nome,',Seu Peso está Normal')
    elif imc <= 29.9:
            print(nome,',Você Está Sobrepeso')
    elif imc <= 34.9:
        print(nome,',Você Está Com Obesidade Grau I')
    elif imc <= 39.9:
        print(nome,',Você Está Com Obesidade Grau II')
    else:
        print(nome,',Você Está Com Obesidade Grau III')

    opcao = input('Deseja calculcar novamente ? S - Sim | N - Não\n').lower()
    if opcao == 's':
        continue
    elif opcao == 'n':
        ('Saindo do sistema!')
    '''
'''
print(40*"_",'Cadastro de Usuario 2º DS',40*'-')
nome = input("Digite o seu nome: ").upper()
CPF = input('Digite o seu CPF: ')
Idade = input("")
Num = input('Digite o seu número: ')
data_nasc = float(input('Digite seu ano de nascimento: '))

while True:
    print(40*"_",'Sistema Console 2º DS',40*'-')
    print()
    print('1 - Calculadora IMC')
    print('2 - Maioridade')
    print('3 - Calculadora')
    print('4 - Dados pessoas')
    print('5 - Feliz Natal')
    print('6 - Sair')

    opcao = input('Digite uma opção: ')

    if opcao == "1":
        nome = (input('Digite o seu nome:'))
        peso = float(input('Digite seu peso: ').replace(',','.'))
        altura = float(input('Digite sua altura:').replace(',','.'))

        imc = peso / (altura * altura)
        print()
        print(f'Seu IMC é:{imc:.2f}')

        if imc <= 18.5:
            print(nome,',Seu Peso está Abaixo do normal')
        elif imc <= 24.9:
            print(nome,',Seu Peso está Normal')
        elif imc <= 29.9:
            print(nome,',Você Está Sobrepeso')
        elif imc <= 34.9:
            print(nome,',Você Está Com Obesidade Grau I')
        elif imc <= 39.9:
            print(nome,',Você Está Com Obesidade Grau II')
        else:
            print(nome,',Você Está Com Obesidade Grau III')

    elif opcao == "2":
        ano_atual = 2025
        idade = ano_atual - data_nasc
        print(nome, 'é maior de idade.' if idade >= 18 else 'é menor de idade.')     
    elif opcao == '3':
        print("Calculadora")
        while True:
            numero1 = int(input('Digite o Primeiro Número: '))
            numero2 = int(input('Digite o Segundo Número: '))
            print('1 - Soma')
            print('2 - Divisão')
            print('3 - Subtração')
            print('4 - Multiplicação')
            print('5 - Sair')
            opcao_calculo = input("Escolha a operação: ")

            if opcao_calculo == "1":
                print(f"Resultado da soma é:  {numero1 + numero2}")
            elif opcao_calculo == "2":
                print(f"Resultado da subtração é:  {numero1 - numero2}")
            elif opcao_calculo == "3":
                print(f"Resultado da divisão é:  {numero1 / numero2}")
            elif opcao_calculo == "4":
                print(f"Resultado da multiplicação é:  {numero1 * numero2}")
            elif opcao_calculo == "5":
                break
        
    elif opcao == '4':
        print(50*'-')
        print(f'Nome: {nome}| Telefone: {CPF}')
        print(f': {Num}| Ano de Nascimento: {data_nasc}')
        print(20*'-')
    elif opcao == '5':
        linhas = 20
        j = 1
        
        while j <= linhas:
            espacos = linhas - j
            estrelas = 2*j - 1
            print('' * espacos + '7' * estrelas)
            j +=1

    elif opcao == '6':
        print('Saindo do sistema!')
        break
    else:
        print('Opção Invalida')

'''
nome = "Joao"
for i in range (5):