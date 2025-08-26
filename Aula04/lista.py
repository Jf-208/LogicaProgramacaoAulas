#Lista
'''
nomes_lista = ['Funalo', 'Cicrano', 'Beltrano', 'Joano', 'Mario', 'Mariano']

print(nomes_lista[0]) #Exibindo o primeiro nome da lista
print(nomes_lista[2]) #Exibindo o segundo nome da lista
print(nomes_lista[5]) #Exibindo o quinto nome da lista

for nome in nomes_lista:
    print(nome)
'''
'''
nomes_lista = ['Funalo', 'Cicrano', 'Beltrano', 'Joano', 'Mario', 'Mariano']
#Percorrendo a lista com um contador
for i in range(len(nomes_lista)):
    print(f'{i + 1}º nome da lista: {nomes_lista[i]}')
'''
'''
nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joano', 'Mario', 'Mariano']
nome = input('Informe o nome que deseja encontrar: ')
#Busca o nome desejado na lista
if nome in nomes_lista:
    print(nome,", Encontrado na lista!")
else:
    print(f'{nome} não encontrado')
#Busca o nome desejado na lista
'''
'''
nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joano', 'Mario', 'Mariano']
nome = input('Informe o nome que deseja encontrar: ')

#Procura pelo indice atráves do valor
indice = nomes_lista.index(nome)

#Retorna o resultado
try:
    print(f'{nome} encontrado no indice {indice}.')
except:
    print(f'{nome} não encontrado.')
'''
'''
nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joano', 'Mario', 'Mariano']
nome = input('Informe o nome que deseja encontrar: ')

#Conta a quantidade de vezes que o valor foi encontrado
quantidade = nomes_lista.count(nome)

#Retorna o resultado
try: print(f'{nome} foi encontrado na lista {quantidade} vezes.')
except:
    print(f'{nome} não encontrado na lista.')
'''
'''
nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joano', 'Mario', 'Mariano']
nome_a_alterar = input('Informe o nome que deseja alterar: ')
nomes_lista[nomes_lista.index(nome_a_alterar)] = input ('Informe o novo nome: ')

for nome in nomes_lista:
    print(nome)
'''
'''
#Tabuada
numero = int(input('Digite o número: '))

for i in range(1, 11):
    resultado = numero * i
    print(f'{i} X {numero} = {resultado}')
'''
