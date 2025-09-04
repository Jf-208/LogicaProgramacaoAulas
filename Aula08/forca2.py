import random
import os

def menu():
    print('1 - Tema:Programa,')
    print('2 - Tema:Comida,')
    print('3 - Tema:Animais,')
    return input("Digite a opção deseja: ")

def escolher_palavras1():

    palavras1 = ['python', 'developer', 'programação', 'inteligencia artificial', 'algoritmo', 
            'computador', 'java', 'linguagens de programação', 'software', 'mouse', 'teclado', 
            'memoria', 'notbook', 'monitor', 'garoto de pgorama', 'programar', 'cooler', 'discord', 'gabinete']
    return random.choice(palavras1)
def escolher_palavras2():

    palavras2 = ["lasanha", "feijoada", "sushi", "pizza", "hambúrguer", "tacos", "estrogonofe", "moqueca", "cuscuz", "churrasco", "risoto", "pastel", "coxinha", "empadão", "yakisoba", "nhoque", "escondidinho", "arroz carreteiro", "bobó de camarão", "tutu de feijão"] 
    return random.choice(palavras2)
def escolher_palavras3():

    palavras3 = ["leão", "tigre", "elefante", "girafa", "zebra", "cavalo", "cachorro", "gato", "lobo", "urso", "coelho", "rato", "macaco", "panda", "jacaré", "cobra", "águia", "papagaio", "golfinho", "tubarão"]
    return random.choice(palavras3)
def sair():
    exit()

def menu():
    p = 

while True:
        palavra_escondida = ''
        for letra in escolher_palavras1:
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


while True:

    match menu():
        case '1':
            exibir_dados()
        case '2':
            criar_conta()  
        case '3':
            depositar()  
        case '4':
            ("Saindo do Sistema....")
            break
        case _:
            print('Opção invalida.')

