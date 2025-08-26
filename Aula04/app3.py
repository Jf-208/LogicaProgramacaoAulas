''''
programa: Sorteio V.2.0
Importando bibliotecas
Aula04: 19/08/2025
Random: Escolha Aleatoria
Descrição: Sistema recebe o nome dos candidatos e realiza o sorteio
'''
#Importando bibliotecas (lib)
import random
lista = []
sair = False

while sair == False:
    nome_candidato = input('Digite os nomes para o sorteio ou enter para sair: ')
    if nome_candidato != "":
        #append - adiciona o valor da variavel na lista
        lista.append(nome_candidato)
    else:
        sair = True
escolhido = random.choice(lista)
print('O Candidato escolhido foi', escolhido)