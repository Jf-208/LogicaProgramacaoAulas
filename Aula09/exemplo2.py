import random
import os
import json
#Importando o random, os e o arquivo json
with open(fr'C:\Users\ead\Desktop\Aulaprogramacao2\LogicaProgramacaoAulas-main\Aula08\forc.json','r', encoding="utf-8") as f:
#Abre o caminho e vai para o arquivo
    temas = json.load(f)
def sair():
    exit()

def menu():
#Menu
    while True:
        p = [["1 - Programação"],
            ["2 - Comida"],
            ["3 - Animais"],
            ["4 - Sair do sistema"]]
        for i in p:
            print(i)
        opcao = input('Informe a opção desejada: ')
        match opcao:
            case '1':
                return random.choice(temas["Tema01"])
            case '2':
                return random.choice(temas["Tema02"])
            case '3':
                return random.choice(temas["Tema03"])
            case '4':
#Puxa os temas do arquivo json e usa o random choice
                return sair()
            case _:
                continue
                
            
def jogar_forca():
    palavra = menu()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6
#ve as palavras corretas e incorretas e define as tentativas do tema escolhido
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
#Diminui as tentativas se a palavra foi errada ou deixa estabilizada
        if palavra_escondida == palavra:
            print('Parabéns, você ganhou!')
            break
        elif tentativas == 0:
            print('Você perdeu! A palavra era:', palavra)
            break
#manda se voce perdeu ou ganhou
        letra_usuario = input('Digite uma letra: ').lower()

        if letra_usuario in palavra:
            print('Letra correta!')
            letras_corretas.append(letra_usuario)
        else:
            print('Letra Errada!')
            letras_erradas.append(letra_usuario)
            tentativas -= 1
#Verifica as palavras digitadas
if __name__ == '__main__':
    os.system('cls')
    print('Bem vindo ao jogo da forca!!')
    jogar_forca()
#coloca a main e manda a base do jogo das palavras corretas e incorretas