

print(30*'-',"Calcule o Juros Simples!",30*'-')

while True:

    capital = int(input('Insira o Capital: '))
    jurosi = float(input('Insira o Juros: '))
    tempo = int(input('Insira o Tempo: '))
    jurosic = jurosi / 100


    jrs = capital * jurosic * tempo
    print()
    print(f'O valor do juros simples e: {jrs}')

    opcao = input('Deseja calculcar novamente ? S - Sim | N - Não\n').lower()
    if opcao == 's':
        continue
    elif opcao == 'n':
        ('Saindo do sistema!')
    break
