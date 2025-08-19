''''
Programa: Sorteio V.1.0
Importando bibliotecas
Aula04: 19/08/2025
Random: Escolha Aleatoria
Descrição: Sistema recebe o nome dos candidatos e realiza o sorteio
'''
#Importando bibliotecas (lib)
import random
nome1 = input('Digite o nome do primeiro candidato: ')
nome2 = input('Digite o nome do segundo candidato: ')
nome3 = input('Digite o nome do terceiro candidato: ')
nome4 = input('Digite o nome do quarto candidato: ')
nome5 = input('Digite o nome do quinto candidato: ')
candidatos = [nome1, nome2, nome3, nome4]

escolhido = random.choice(candidatos)
print(f'O Candidato escolhido foi: {escolhido}')
