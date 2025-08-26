print(30*'-',"Consumo Médio do Veiculo",30*'-')

dtp = int(input('Insira a distancia percorrida (KM): '))
cbg = int(input('Insira a quantidade de combustivel gasto (L): '))

cmv = dtp / cbg 

print(f'A média do veiculo foi {cmv} quilômetros por litro')
