'''
int() → converte um valor para número inteiro.

float() → converte um valor para número decimal.

input() → lê uma entrada digitada pelo usuário.

if / elif / else → estruturas de decisão (condições).
    
while True: → cria um laço infinito até usar break.

break → interrompe o loop.

entrada.lower() → transforma a entrada em minúscula (assim aceita Fim, FIM etc).

try / except → tratamento de erros (evita travar com valor inválido).

ValueError → erro quando a conversão de número falha.

+= → soma o valor à variável existente.

contador → conta quantos salários foram digitados.

if contador > 0: → evita divisão por zero.

:.2f → formata o número com 2 casas decimais.

print() → mostra algo na tela.

[] → cria uma lista vazia.

append() → adiciona um item ao final da lista.

remove() → remove um item específico da lista.

in → verifica se um elemento está na lista.

len() → retorna o tamanho da lista (quantos itens tem).

for i, f in enumerate(lista, start=1): → percorre a lista mostrando índice e valor.

enumerate() → gera pares (posição, valor) para usar em loops.

break → interrompe o loop.

len(senha) → conta quantos caracteres a string tem.

upper() → converte todos os caracteres para maiúsculos.

lower() → converte todos os caracteres para minúsculos.

isdigit() → retorna True se o caractere for um número (0–9).

any() → retorna True se pelo menos um item da lista/loop for verdadeiro.

for ch in senha → percorre cada caractere da string.

max(lista) → retorna o maior valor da lista.

min(lista) → retorna o menor valor da lista.

sum(lista) → soma todos os elementos da lista.

len(lista) → retorna a quantidade de elementos da lista.

total / len(vendas) → cálculo da média (soma ÷ quantidade).

:.2f → formata número decimal com 2 casas.

vendas.append(valor) → adiciona cada venda digitada na lista.

entrada.lower() → transforma a palavra em minúscula (assim aceita Fim, FIM, fim).

try / except → evita erro caso o usuário digite algo que não seja número.

if len(vendas) > 0: → garante que não vai tentar calcular média sem dados.

{} → cria um dicionário.

"chave": valor → associa cada produto às suas informações.

dicionario[chave] → acessa o valor correspondente à chave.

estoque.items() → percorre o dicionário mostrando (chave, valor).

lower() → transforma a entrada em minúsculas (evita erro de maiúsculas/minúsculas).

int() → converte para número inteiro (quantidade).

float() → converte para número decimal (preço).

O que capitalize() faz

str.capitalize() retorna uma nova string onde apenas o primeiro caractere da string é transformado em maiúsculo e todos os outros caracteres ficam em minúsculo.

Strings são imutáveis, então s.capitalize() não altera s a menos que você reatribua (ex.: s = s.capitalize()).

dicionario.keys() → retorna todas as chaves do dicionário (usado para verificar produtos e listar).

capitalize() → deixa primeira letra maiúscula e o resto em minúscula.

dicionario.pop(chave) → remove o item do dicionário.

float() → converte para número decimal (preço).

int() → converte para número inteiro (quantidade).

lower() → transforma texto em minúscula para uniformizar entradas.

dict.keys() → retorna todas as chaves do dicionário.

dict.values() → retorna todos os valores do dicionário (informações de cada produto).

capitalize() → coloca a primeira letra maiúscula e o restante minúsculo.

pop(chave) → remove um item do dicionário pela chave.

float() → converte para número decimal (preço).

int() → converte para número inteiro (quantidade).

lower() → transforma texto em minúscula para uniformizar entradas.

dict.pop(chave)

Remove a chave e o valor associado do dicionário.

Retorna o valor removido (opcional).

Listas ([]) → armazenam todos os funcionários.

Dicionários ({}) → guardam dados de cada funcionário (nome, idade, salario).

append() → adiciona um novo funcionário na lista.

len() → conta quantos funcionários existem.

sum() → soma os salários para calcular a folha.

max() / min() → encontram o funcionário com maior/menor idade ou salário.

for ... in enumerate(...) → percorre a lista mostrando índice e informações.

try / except → evita erros quando usuário digita valores inválidos.

:.2f → formata números decimais com 2 casas.

lambda x: x["idade"] / x["salario"] → define critérios para max() e min().

strip() → remove espaços extras no início/fim do nome digitado.

if / elif / else → controla as opções do menu.

lambda cria uma função anônima (ou seja, sem nome) de forma rápida.

lambda é uma forma curta de criar funções temporárias, geralmente usadas como argumento de outras funções como max(), min(), sorted(), filter(), map().

Evita precisar criar uma função separada só para passar como critério.
'''