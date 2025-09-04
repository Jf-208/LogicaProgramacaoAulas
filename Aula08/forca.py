import random
import os


def escolher_palavras():

    palavras = ['python', 'developer', 'programação', 'inteligencia artificial', 'algoritmo', 
            'computador', 'java', 'linguagens de programação', 'software', 'mouse', 'teclado', 
            'memoria', 'notbook', 'monitor', 'garoto de pgorama', 'programar', 'cooler', 'discord', 'gabinete']
            
#Aqui guardamos as palavras

    return random.choice(palavras)
#Aqui ele escolhe uma palavra aleatoria

def jogar_forca():
    palavra = escolher_palavras()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6 
#Função que guarda as partes do jogo
    while True:
        palavra_escondida = ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_escondida += letra
            else:
                palavra_escondida += '_'

        print('Palavra:', palavra_escondida)
        print('Letras erradas:', letras_erradas)
        print('Tentativas restantes:', tentativas)

        if palavra_escondida == palavra:
            print('Parabéns! Você ganhou!!!')
            break
        elif tentativas == 0: 
            print('Você perdeu! A palavra era:', palavra)
            break

        letra_usuario = input('Digite uma letra: ').lower()

        if letra_usuario in palavra:
            print('Letra correta!')
            letras_corretas.append(letra_usuario)
        else:
            print('Letra errada!')
            letras_erradas.append(letra_usuario)
            tentativas -= 1

if __name__=='__main__':
    os.system('cls')
    print('Bem vindo ao jogo da forca')
    jogar_forca()