lista = []
pares = []
impares = []

while True:
    lista.append(int (input ('Declare o núemero: ')))
    
    while True:
        fim = str (input ('Ainda quer continuar ? '.upper())).upper()[0]
        if fim in 'SN':
            break
    if fim in 'N':
        break

for p in lista:
    if p % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)

print (f'\nOs valores mensionados foram: {lista}')
print (f'A lista de números pares: {pares}')
print (f'Lista de números impares: {impares}')
