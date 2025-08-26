print(30*'-',"Diferença de valores",30*'-')

while True:

    num1 = int(input('Insira o primeiro número: '))
    num2 = int(input('Insira o segundo número: '))
    
    if num1 != num2:
        print('Esses números são diferentes!')
    else:
        print('Eles são iguais!')

    opcao = input('Deseja ver a diferença novamente ? S - Sim | N - Não\n').lower()
    if opcao == 's':
        continue
    elif opcao == 'n':
        ('Saindo do sistema!')
    break

