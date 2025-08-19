'''
Programa: Contagem Regressiva
    Importando bibliotecas
    Aula 04: 19/08/2025
'''
#Importando bibliotecas (lib)
import os
from time import sleep 

cont = input('Digite um numero inteiro: ')

try: 
    cont_int = int(cont)
    while cont_int >= 0:
        os.system("cls")
        print(f'Contagem Regressiva: {cont_int}')
        sleep(0.01)  # Pausa de 1 segundo
        cont_int -= 1
except:
    print('Por favor, digite um número inteiro válido.')
print('Contagem finalizada!')