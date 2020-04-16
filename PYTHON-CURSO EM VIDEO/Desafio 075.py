num = (int(input('Digite um número: ')),
       int(input('Digite outro: ')),
       int(input('Digite mais outro: ')),
       int(input('Informe o ultimo número: ')))

n9 = num.count(9)

cont = 0 
if not n9 == 0:
    print(f'O núemero 9 apareceu {n9} vezes')
else:
    print ('O número 9 NÃO foi encontrado nenhuma vez...')
    
if 3 in num:
    print(f'O primeiro número 3 apareceu na {num.index(3) + 1}° posição')
else:
    print ('O valor 3 não foi encontrado entre os números')

print ('Os números pares que foram encontrados:', end=' ')

for i in num:
    if i % 2 == 0:
        print (i,end=' ')
