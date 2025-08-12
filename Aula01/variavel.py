'''
nome = "João Felipe Ribeiro" 
idade = "17 anos"
dat_nasc = "05/07/2008"
print ("Nome:",nome)
print ("Idade:",idade)
print ("Data de Nascimento:",dat_nasc)
print("Olá me chamo", nome,"tenho", idade,"e nasci no dia", dat_nasc)
# Mostra a idade nome e a data de nascimento
# tipos de variaveis

nome = "joao"
idade = 17
altura = 1.77
ativo = True
print("o tipo de variavel nome é:", type(nome))
print("o tipo de variavel idade é:", type(idade))
print("o tipo de variavel altura é:", type(altura))
print("o tipo de variavel ativo é:", type(ativo))
# Mostra os tipos de variaveis
print()
#Operadores
print(30*'-',"operadores aritmeticos",30*"-")
num1 = 1241
num2 = 124
# seta as variaveis de numeros e quais serão calculados

soma = num1 + num2 
divi = num1 / num2
divisao_inteira = num1 // num2 
expo = num1 ** num2
mult = num1 * num2 
subt = num1 - num2 
resto = num1 %2 
# aqui temos as operações incluindo exponencial e o resto da divisão
print("Resultado da soma", num1, "+", num2, 'é:', soma)
print("Resultado da divisão", num1, "/", num2, 'é:', divi)
print("Resultado da divisão inteira", num1, "//", num2, 'é:', divisao_inteira)
print("O resto", num1, "/", num2, 'é:', resto)
print("Resultado da multiplicação", num1, "*", num2, 'é:', mult)
print("Resultado da exponenciação", num1, "**", num2, 'é:', expo)
print("Resultado da subtração", num1, "-", num2, 'é:', subt)
# print dos resultados das operações

#Operadores de comparação
print()
print(30*'-',"operadores de comparação",30*"-")
num1 > num2
num1 < num2
num1 == num2
num1 >= num2
num1 <= num2
num1 !=num2

ano = 2025
print('Ano atual', ano)
ano += 1
print('Ano acrecido de +1:', ano)
ano -= 1
print ("Ano decrecido de -1:", ano)


adiciona mais um e tira mais um ao 2025 (OBS: de cima pra baixo se inverter a ordem ele muda
ano = 2025 e print depois. tudo que esta em baixo acontece de cima pra baixo por isso a mesma variavel


#Operadores Logicos AND, OR, NOT

#Entrada de dados
print()
print(30*'-',"Entrada de Dados",30*"-")

nome_usuario = input("Digite o seu nome: ")
#Função que recebe dados
print("Seja Bem-vindo ao Sistema Python,", nome_usuario,"!!!")

#Calculadora
print()
print(30*'-',"Calculadora",30*"-")

numero1 = int(input('Digite o Primeiro Número: '))
numero2 = int(input('Digite o Segundo Número: '))
#int faz a conta dar certo
#str ele buga e faz 10 + 10 = 1010
soma = numero1 + numero2 
divi = numero1 / numero2 
mult = numero1 * numero2 
subt = numero1 - numero2 
#variaveis dos numeros

print("Resultado da soma", numero1, "+", numero2, 'é:', soma)
print("Resultado da divisão", numero1, "/", numero2, 'é:', divi)
print("Resultado da multiplicação", numero1, "*", numero2, 'é:', mult)
print("Resultado da subtração", numero1, "-", numero2, 'é:', subt)
#print das operacoes etc

#tipos de dados
#float = numeros reais, ou seja, tem ',' , exemplo: 5.20 
#int = numeros inteiros
#str = texto, conjunto de caracteres
#bool = valores logicos como true e false
'''
print()
print(30*'-',"Convertendo tipos de dados",30*"-")

ano_nascimento = input('Digite o seu ano de nascimento: ')
print(type(ano_nascimento))
#Convertendo para inteiro
ano_nascimento = int(ano_nascimento)
print(type(ano_nascimento))
#data de nascimento
n1 = 10
n2 = 20

print("A soma é:", n1+n2, type(n1), float(n2))
#Soma de numeros e numeros com virgula
saudacao = input('Digite seu nome: ')
cpf = input('Digite o seu CPF: ')
telefone = input('Digite o seu telefone: ')

print(20*'-','Dados Pessoais', 20*'-')
print('Nome:', saudacao)
print('CPF: ', cpf, '| Telefone:', telefone)
print(56*'-')
#dados 
