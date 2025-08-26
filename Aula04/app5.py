''''
Programa: Sorteio V.4.0
Importando bibliotecas
Aula04: 19/08/2025
Random: Escolha Aleatoria
Descrição: Sistema recebe o nome dos candidatos e realiza o sorteio
'''

#Importando bibliotecas (lib)
from random import randint
print("Tente adivinhar o numero!")
num1 = int(input("Digite um número: "))
num_secreto = randint(1, 100)

if num1 == num_secreto:
    print("Parabéns, você ganhou! ")
else: 
    print("Você perdeu")
    print(f"O número secreto e: {num_secreto}")          