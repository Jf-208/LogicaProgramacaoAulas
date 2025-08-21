import json
try:
    arquivo = input('Digite um nome ').strip().lower()

    with open(f'{arquivo}.json', 'r', encoding= 'utf-8') as f:
        dados = json.load(f)

    print(f'{'_'*20} DADOS {'-'*20}\n ')
    for dado 