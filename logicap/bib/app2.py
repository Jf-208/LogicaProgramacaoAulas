import json
import os


class Livro:
    #Selecionamos a caracteristica do objeto
    def __init__(self, id, titulo, autor, ano):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    #transformando em dicionario
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano
        }


class Biblioteca:
    def __init__(self, arquivo_json="biblioteca.json"):
        self.arquivo_json = arquivo_json
        self.livros = self._carregar()
    #Lê o arquivo JSON e transforma cada livro salvo em um objeto Livro novamente.
    def _carregar(self):
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Livro(**livro) for livro in data]
        return []
    #Salva o cadastro no arquivo JSON
    def _salvar(self):
        with open(self.arquivo_json, "w", encoding="utf-8") as file:
            json.dump([livro.to_dict() for livro in self.livros], file, indent=4, ensure_ascii=False)
    #ID automatico
    def _proximo_id(self):
        if not self.livros:
            return 1
        return max(livro.id for livro in self.livros) + 1
    #Cadatro fo livro
    def cadastrar(self, titulo, autor, ano):
        novo_id = self._proximo_id()
        #A dependencia acontece aqui, pois a biblioteca precisa da classe livro para executar a ação
        livro = Livro(novo_id, titulo, autor, ano)
        self.livros.append(livro)
        self._salvar()
        print(" Livro cadastrado com sucesso!")
    #Atualiza o livro
    def atualizar(self, id, novo_titulo=None, novo_autor=None, novo_ano=None):
        for livro in self.livros:
            if livro.id == id:
                if novo_titulo: livro.titulo = novo_titulo
                if novo_autor: livro.autor = novo_autor
                if novo_ano: livro.ano = novo_ano
                self._salvar()
                print(" Livro atualizado!")
                return
        print(" Livro não encontrado!")
    #Deletando o livro da lista 
    def deletar(self, id):
        for livro in self.livros:
            if livro.id == id:
                self.livros.remove(livro)
                self._salvar()
                print(" Livro deletado!")
                return
        print(" Livro não encontrado!")
    #Listando a biblioteca
    def listar(self):
        if not self.livros:
            print(" Nenhum livro cadastrado.")
            return
        for livro in self.livros:
            print(f"{livro.id} -\n {livro.titulo} ({livro.autor}, {livro.ano})")

#MENU
def menu():
    #Chamando classe
    biblioteca = Biblioteca()

    while True:
        print("\n1 - Cadastrar Livro")
        print("2 - Listar Livros")
        print("3 - Atualizar Livro")
        print("4 - Deletar Livro")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano: ")
            biblioteca.cadastrar(titulo, autor, ano)

        elif opcao == "2":
            biblioteca.listar()

        elif opcao == "3":
            id = int(input("ID do livro para atualizar: "))
            novo_titulo = input("Novo título (ou Enter para manter): ")
            novo_autor = input("Novo autor (ou Enter para manter): ")
            novo_ano = input("Novo ano (ou Enter para manter): ")
            biblioteca.atualizar(id, novo_titulo or None, novo_autor or None, novo_ano or None)

        elif opcao == "4":
            id = int(input("ID do livro para deletar: "))
            biblioteca.deletar(id)

        elif opcao == "5":
            print(" Saindo...")
            break

        else:
            print(" Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
