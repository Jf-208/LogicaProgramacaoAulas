import os

while True:
    try:
        novo_texto = input('Digite um texto: \n')
        novo_arquivo = input('Digite o nome do arquivo (sem extensão): ').strip().lower()

        with open (fr'C:\Users\JoaoFelipeRibeirodeO\Documents\LogicaProgramaçãoAulas\Aula05/{novo_arquivo}.txt', 'w', encoding = 'utf-8') as f:
            f.write(novo_texto)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{novo_arquivo}.txt gravado com sucesso ')

        while True:
            prosseguir = input('Deseja abrir outro arquivio ?(s/n)').strip().lower()
            if prosseguir == 's' or prosseguir == 'n':
                break
            else:
                print('Opção Inválida')
            continue
        match prosseguir:
            case 's':
                continue
            case 'n':
                break


    except Exception as e:
        break

        
