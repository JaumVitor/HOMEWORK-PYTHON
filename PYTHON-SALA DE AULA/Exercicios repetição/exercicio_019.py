from time import sleep

print('DIGITE 0 NA IDENTIFICAÇÃO, CASO QUEIRA PARAR DE ANÁLISAR')
print ('')

id = 1
peso = contador = peso_menor = peso_maior = 0

while not id == 0:
    id = int(input('Identificação do boi ?'))
    
    if id == 0:
        break
    peso = float ( input ('Digite o peso : '))
    print ('')

    if contador == 0:
        peso_maior = peso
        peso_menor = peso
    
    contador += 1
    
    if peso > peso_maior:
        peso_maior = peso
    if peso < peso_menor:
        peso_menor = peso

print ('CARREGANDO...\n')
sleep(3)

print(
    f'O maior peso é {peso_maior}Kg')
print(
    f'E o menor peso é {peso_menor}Kg')