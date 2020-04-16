numeros = [[],[]]

for n in range(7):
    valor = int (input ('Digite o valor: '))
    
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
         
numeros[0].sort
numeros[1].sort

print()

print (f'Os números pares foram: {numeros[0]}')
print (f'Os números impares foram: {numeros[1]}')

