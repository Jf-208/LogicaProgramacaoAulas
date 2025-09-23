# nome e vida - atacar
# self - quando quero me referir a algum atributo da classe
# construtor - quando quero criar um novo objeto, chamo o construtor para acessar os atributos
# 1 _ pra protegido 2 __ pra privado 
# Herança: Agora, vamos criar tipos de personagens que herdam caracteristícas dos personagens originais 
import time
print("\n" + "-"*30)
print("         VAGABOND")
print("-"*30 + "\n")
time.sleep(2)

class Ronin:
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


    def atacar(self, personagem):
        personagem.vida -= 90
        print(f'{self.nome} executou o golpe contra o {personagem.nome}.')

        
        if personagem.vida <= 0:
            match personagem.nome:
                case "Arqueiro":
                    print(f"É com um giro ágil, {self.nome} desfere o corte final, cravou sua lâmina no coração do {personagem.nome}.")

        if personagem.vida <= 0:
            match personagem.nome:
                case "Samurai":
                    print(f'A lâmina corta o ar em silêncio, e quando repousa, {personagem.nome} já não respira mais.')

        print(f'Agora {personagem.nome} está com {personagem.vida} de vida')

class Samurais(Ronin):
    def __init__(self, nome, vida, armadura=False):
        super().__init__(nome, vida)
        self.__armadura = armadura

    @property
    def armadura(self):
        return self.__armadura
    
    @armadura.setter
    def armadura(self, armadura):
        self.__armadura = armadura

    # sobrescrevendo o metodo da class pai
    def atacar(self, personagem):
        personagem.vida -= 50
        print(f'O {self.nome} executou um golpe forte contra {personagem.nome}.')
        print(f'Que agora está com {personagem.vida}')
    
    def proteção(self):
        self.__vida += 30

    def desviar2(self, personagem):
        print(f'O {self.nome} desfereriu a lamina contra {personagem.nome} que rapidamente evitou do ataque!')
#
class Arqueiro(Ronin):
    def __init__(self, nome, vida, armadura=False):
        super().__init__(nome, vida)
        self.__armadura = armadura

    @property
    def armadura(self):
        return self.__armadura
    
    @armadura.setter
    def armadura(self, armadura):
        self.__armadura = armadura

    def atirar(self, personagem):
        personagem.vida -= 40
        print(f'O {self.nome} dispara uma flecha rapida contra {personagem.nome}')
        print(f'A vida de {personagem.nome} agora é de {personagem.vida}')

    def proteção(self):
        self.__vida += 30

    def desviar(self, personagem):
        print(f'O {self.nome} Dispara contra {personagem.nome} que por pouco conseguio desviar do disparo!')

Samurai = Samurais('Samurai', 150)
Kyudo = Arqueiro('Arqueiro', 120)
Musashi = Ronin('Musashi', 350)


Samurai.atacar(Musashi)
time.sleep(1.4)
Kyudo.atirar(Musashi)
time.sleep(1.4)
Musashi.atacar(Samurai)
time.sleep(1.4)
Musashi.atacar(Kyudo)
time.sleep(1.4)
Kyudo.desviar(Musashi)
time.sleep(1.4)
Samurai.desviar2(Musashi)
time.sleep(1.4)
Musashi.atacar(Kyudo)
time.sleep(1.4)
Musashi.atacar(Samurai)
time.sleep(2)

print("\n" + "-"*96)
print(f'A poeira da batalha se dissipa, e no silêncio eterno, apenas o nome de Musashi ecoa como vencedor.')