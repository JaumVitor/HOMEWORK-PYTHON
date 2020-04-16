x = 'S'
mult = 0
soma = 0

while not x in 'N':
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Outro número: '))

    for i in range (1, n2 + 1):
        mult += n1
    print(mult)
    soma += mult
    
    mult = 0

    x = str(input('Quer continuar S/N ? ')).strip().upper()[0]
    print ('')

    if x in 'Nn':
        break
    
    if not x in 'NnSs':
        while not x in 'NnSs':
            x = str (input ('Quer continuar S/N ? ')).strip().upper()[0]

print (f'Soma da multiplicação dos números = {soma}')

