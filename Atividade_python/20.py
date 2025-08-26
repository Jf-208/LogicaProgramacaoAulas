print(30*'-',"Conversão",30*'-')

num1 = int(input('Insira o valor de metros: '))

cent = num1 * 100
milimet = num1 * 1000
km = num1 / 1000

print(f'{num1} metros virou {cent} centimetros')
print(f'{num1} metros virou {milimet} milimetros')
print(f'{num1} metros virou {km} quilômetros')