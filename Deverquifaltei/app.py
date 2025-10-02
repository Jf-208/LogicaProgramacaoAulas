import json
import os

# ==============================
# CLASSE LIVRO (molde dos livros)
# ==============================
class Livro:
    def __init__(self, id, titulo, autor, ano):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

# ===================================================
# CLASSE BIBLIOTECA (guarda os livros e faz o CRUD)
# ===================================================
class Biblioteca:
    def __init__(self):
        self.arquivo = "banco_livros.json"
        self.livros = self.carregar_livros()

    def carregar_livros(self):
        if not os.path.exists(self.arquivo):
            return []
        try:
            with open(self.arquivo, "r", encoding="utf-8") as file:
                dados = json.load(file)
                return dados if isinstance(dados, list) else []
        except:
            return []

    def salvar_livros(self):
        with open(self.arquivo, "w", encoding="utf-8") as file:
            json.dump(self.livros, file, indent=4, ensure_ascii=False)

#Criar (Cadastrar livro)
    #Criar (Cadastrar livro)
    def cadastrar(self):
        #Verificação do número do livro (apenas números)
        while True:
            id_livro = input("Digite um número para cadastrar o livro: ").strip()
            if not id_livro.isdigit():
                print("Número inválido. Digite apenas números.")
                continue

            # Verifica se o número do livro já existe
            id_existente = False
            for livro in self.livros:
                if livro['id'] == id_livro:
                    print("Esse número já está cadastrado para outro livro. Digite outro.")
                    id_existente = True
                    break

            if not id_existente:
                break  # Sai do loop quando o número é válido e não repetido

        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()

        #Verificação do ano do livro (somente números)
        ano = input("Ano: ").strip()
        while not ano.isdigit():
            print("Ano inválido. Digite apenas números.")
            ano = input("Ano: ").strip()

        livro = Livro(id_livro, titulo, autor, ano)
        self.livros.append(livro.__dict__)
        self.salvar_livros()
        print("Livro cadastrado com sucesso.")

#Lista os livros e verifica se existe ou não
    def listar(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        for livro in self.livros:
            print(f"[{livro['id']}] {livro['titulo']} - {livro['autor']} ({livro['ano']})")

#Atualiza os livros e também com a função de verificar o ano e se o livro foi encontrado ou não
    def atualizar(self):
        id_busca = input("Digite o número do livro para atualizar: ").strip()
        for livro in self.livros:
            if livro['id'] == id_busca:
                novo_titulo = input("Novo título: ").strip() or livro['titulo']
                novo_autor = input("Novo autor: ").strip() or livro['autor']

                novo_ano = input("Novo ano: ").strip()
                if novo_ano == "":
                    novo_ano = livro['ano']
                else:
                    while not novo_ano.isdigit():
                        print("Ano inválido. Digite apenas números.")
                        novo_ano = input("Novo ano: ").strip()

                livro['titulo'] = novo_titulo
                livro['autor'] = novo_autor
                livro['ano'] = novo_ano

                self.salvar_livros()
                print("Livro atualizado.")
                return

        print("Livro não encontrado.")
#Exclui o livro desejado e também verifica se o livro foi encontrado ou não
    def excluir(self):
        id_busca = input("Digite o número do livro para excluir: ").strip()
        for livro in self.livros:
            if livro['id'] == id_busca:
                self.livros.remove(livro)
                self.salvar_livros()
                print("Livro removido.")
                return
        print("Livro não encontrado.")

# =========================================
# MENU PRINCIPAL (interface com o usuário)
# =========================================
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n====== SISTEMA DE BIBLIOTECA ======")
        print("1 - Cadastrar Livro")
        print("2 - Listar Livros")
        print("3 - Atualizar Livro")
        print("4 - Excluir Livro")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            biblioteca.cadastrar()
        elif opcao == "2":
            biblioteca.listar()
        elif opcao == "3":
            biblioteca.atualizar()
        elif opcao == "4":
            biblioteca.excluir()
        elif opcao == "5":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

# =============================
# INICIAR O PROGRAMA
# =============================
if __name__ == "__main__":
    menu()
