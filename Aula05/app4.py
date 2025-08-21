import os

while True:
    try:
        novo_texto = input('Digite um texto: \n')

        # Sempre grava no arquivo texto.txt
        with open(r'C:\Users\JoaoFelipeRibeirodeO\Documents\LogicaProgramaçãoAulas\Aula05\texto.txt', 'w', encoding='utf-8') as f:
            f.write(novo_texto)

        os.system('cls' if os.name == 'nt' else 'clear')
        print('texto.txt gravado com sucesso')

        novo_texto_adicionar = input('Digite o novo texto: \n')

        # Adiciona novo texto ao final do arquivo texto.txt
        with open(r'C:\Users\JoaoFelipeRibeirodeO\Documents\LogicaProgramaçãoAulas\Aula05\texto.txt', 'a', encoding='utf-8') as f:
            f.write(f'\n{novo_texto_adicionar}')
        print('Gravado com sucesso')

        # Lê e mostra o conteúdo final do arquivo texto.txt
        with open(r'C:\Users\JoaoFelipeRibeirodeO\Documents\LogicaProgramaçãoAulas\Aula05\texto.txt', 'r', encoding='utf-8') as file:
            texto_final = file.read()
        print(f'Texto Final: {texto_final}')

        while True:
            prosseguir = input('Deseja abrir novamente? (s/n) ').strip().lower()
            if prosseguir in ['s', 'n']:
                break
            else:
                print('Opção Inválida')
        if prosseguir == 'n':
            break

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        break