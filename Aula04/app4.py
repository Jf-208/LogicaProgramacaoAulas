''''
Programa: Sorteio V.3.0
Importando bibliotecas
Aula04: 19/08/2025
Random: Escolha Aleatoria
Descrição: Sistema recebe o nome dos candidatos e realiza o sorteio
'''
#Importando bibliotecas (lib)
import random
import os
import time 

lista_nome = []
lista_sorteados = []

while True:
    nome = input('Digite o nome para o sorteio: ')
    if nome:
        lista_nome.append(nome)
    else:
        break
while True:
    if lista_nome:
        os.system("cls")
        escolhido = random.choice(lista_nome)
        lista_sorteados.append(escolhido)

        print(f'O Candidato escolhido foi: {escolhido}')

        lista_sorteados.remove(escolhido)

        opcao = input('Deseja sortear novamente? (s/n): ').lower()
        os.system("cls")

        if opcao !='s':
            break
    else:       
        print("Não há nomes para ser sorteados.")
        break
    print('Programa Finalizado')
    print(f'Os nomes sorteadores foram{lista_sorteados}')
