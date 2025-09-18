import json
with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\a\biblioteca.json','r', encoding="utf-8") as f:
    #Abre o caminho e vai para o arquivo
    biblioteca = json.load(f)

json.load(ti)



def deletar():
    global biblioteca

    print('Digite o nome do livro que deseja remover: ')
    for chave, lista in biblioteca.items():
        if livro in lista in biblioteca.items():
            del biblioteca[livro]
        print('livro excluído com sucesso')
    # Verifica se o livro digitado existe, e remove ele
        if not biblioteca:
            print("Livro não encontrado.")
        return 

def atualizar():
    global biblioteca
    remov = input("Digite o título do livro que deseja remover: ").lower()
    # Após receber o título, faz a substituição
    encontrado = False
    for chave, lista in biblioteca.items():
        for livro in lista:
            if livro["titulo"].lower() == remov:
                #coloque as informações
                novo_titulo = input("Digite o novo título: ")
                novo_autor = input("Digite o novo autor: ")
                nova_publi = int(input("Digite o novo ano de publicação: "))
                #atualiza dentro do json
                livro["titulo"] = novo_titulo
                livro["Autor"] = novo_autor
                livro["publicacao"] = nova_publi

                with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas-main\a\biblioteca.json', 'w', encoding="utf-8") as f:
                    json.dump(biblioteca, f, ensure_ascii=False, indent=4)

                print("Livro atualizado com sucesso!")
                encontrado = True
                break
        if encontrado:
            break

    if not encontrado:
        print("Livro não encontrado.")