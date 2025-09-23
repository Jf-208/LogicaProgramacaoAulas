class PersonagemFavorito:
    # construtor
    def __init__(self, nome, vida):
        # encapsulamento
        self.__nome = nome 
        self.__vida = vida

    # definindo GET e SET
    @property
    def nome(self):
        return self.__nome

    # definindo SET
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida


    def atacar(self, personagem1):
        personagem1.vida -= 50
        print(f'{self.nome} Atacou a {personagem2.nome} e tirou 50 da durabilidade da mesma.')
        print(f'Agora está a torre está com: {personagem2.vida}')

    def atacar2(self, personagem2):
        personagem2.vida -= 20
        print(f'{self.nome} Atacou a {personagem1.nome} e tirou 50 de vida dele.')
        print(f'Agora está o Goblin está com: {personagem1.vida}')
            

personagem1 = PersonagemFavorito('Goblin', 50)
personagem2 = PersonagemFavorito('Torre', 2000)

personagem1.atacar(personagem2)
personagem2.atacar2(personagem1)
