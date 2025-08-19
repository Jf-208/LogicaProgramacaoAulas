#Importando lib
import random 
import time
import os

numero_secreto = random.randint(1, 100)

tentativas = 0
max_tentativas = 10
acertou = False

print(30*'-',"Bem-vindo ao Adivinha-Logo!",30*'-')
print(f'Você tem {max_tentativas} tentativas para adivinhar o número secreto entre 1 e 100.')
print('Vamos começar?')

while tentativas < max_tentativas:
    try: 
        # entrada do usuario
        palpite = int(input('Digite o seu palpite: '))
    
    except ValueError:
        print ('Por favor, Digite um número válido')
        continue

    tentativas +=1 

    #Verificar palpite
    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print('Tente um número maior!')
        time.sleep(2)
        os.system('cls')
    else:
        print("Tente um número menor!")
        time.sleep(2)
        os.system('cls')
if acertou:
    print(f"Parabéns você ganhou! Você acertou o numero {numero_secreto} em {tentativas} tentativas")
else:
    print(f'Que pena! Você não conseguiu adivinhar o numero secreto{numero_secreto}')

    #append adiciona um item ao final da lista
    # insert voce escolhe a posicao
    # + 1 pois ele começa do 0
    # remove, remove pelo valor mas so digita um e se tiver mais de um desse item ele continua la
    # join junta
    # split pega os valores da variavel e separa em elementos diferentes de uma lista
    # sum os valores dentro da lista
    # ordem crescente e decrescente sort decrescente sort(reverse-True)
    

