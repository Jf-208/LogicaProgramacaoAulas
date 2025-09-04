import random
import string

def gerar_senha(comprimento=12, incluir_maisculo=True, incluir_minusculo=True,
                incluir_numero=True, incluir_caracter=True):
    
    caracteres = ''
    if incluir_maisculo:
        caracteres += string.ascii_uppercase

    if incluir_minusculo:
        caracteres += string.ascii_lowercase
        
    if incluir_numero:
        caracteres += string.digits
    
    if incluir_caracter:
        caracteres += string.punctuation
        
    if not caracteres:
        return ValueError('Deve ter pelo menos um tipo de caracter')
    
    senha = ''.join(random.choice(caracteres)for _ in range(comprimento))
    print(f'senha: {senha}')
    return senha


def main():
     print('Gerador de senhas fortes')
     comprimento = int(input('Digite o comprimento da senha (padrão é 12): ') or 12)
     incluir_maiuscula = input('Incluir maiúscula (s/n, padrão = sim): ').lower() != 'n'
     incluir_minuscula = input('Incluir minuscula (s/n, padrão = sim): ').lower() != 'n'
     incluir_numero = input('Incluir números (s/n, padrão = sim): ').lower() != 'n'
     incluir_caracter_esp = input('Incluir caracteres especiais (s/n, padrão = sim): ').lower() != 'n'

     senha = gerar_senha(comprimento, incluir_maiuscula, incluir_minuscula, 
                         incluir_numero, incluir_caracter_esp)
     
     print(f'A senha gerada foi: {senha}')

     with open('senhas.txt', 'a') as s:
        s.write(f'/n{senha}')
    #Tem que rodar o terminal fora do aula08 para

if __name__=='__main__':
    main()
#Selecionar a main 
#Vai executar e achar o if name esse e o principal do projeto se não pode ser um modulo do principal