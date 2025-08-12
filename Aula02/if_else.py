
#Estrutura de decisão

nome = input('Digite o seu nome:')
idade = int(input('Digite sua idade:'))

print('Antes do if')
if idade >= 18:
    print('Número Par')
else:
    print('Número Impar')

print(40*"-", "BOLETIM ESCOLAR", 40*"-")
nome_aluno = (input("Digite o nome do aluno: ")).upper()
nota1 = float(input("Digite a sua primeira nota:"))
nota2 = float(input("Digite a sua segunda nota:"))
nota3 = float(input("Digite a sua terceira nota:"))
nota4 = float(input("Digite a sua quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4)/4
# >= 7: aprovado
# >= 5: recuperação
# reprovado

if media >= 7: 
    print(f'{nome_aluno} !!!Aprovado!!!')
    print(f'Nota 1: {nota1} | Nota 2: {nota2}')
    print(f'Nota 3: {nota3} | Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')
elif media >= 5:
    print(f'{nome_aluno} !Recuperação!')
    print(f'Nota 1: {nota1} | Nota 2: {nota2}')
    print(f'Nota 3: {nota3} | Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')
else:
    print(f'{nome_aluno} !Reprovado!')
    print(f'Nota 1: {nota1} | Nota 2: {nota2}')
    print(f'Nota 3: {nota3} | Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')


#Requisitos Mínimos 
nome = input('Digite o seu nome:')
idade = int(input('Digite sua idade aqui: '))
altura = float(input('Digite sua altura:'))

#Verificação
if idade >= 12 and altura >= 1.2 :
    print(f'A entrada de {nome} está autorizada.')
else: 
    print(f'A entrada de {nome} não está autorizada. ')


#variaveis 
nome = input("Digite o seu nome: ")
idade = int(input ("Digite sua idade: "))
#Operador ternário 
print(nome, 'é maior de idade.' if idade >= 18 else 'é menor de idade.')