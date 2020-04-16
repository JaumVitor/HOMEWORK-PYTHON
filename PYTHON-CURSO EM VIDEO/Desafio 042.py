l1 = int ( input ('Primeiro lado : '))
l2 = int ( input('Segundo lado : '))
l3 = int ( input ('Terceiro lado : '))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('Pode formar triangulo')

    if l1 == l2 == l3:
        print('Triangulo Equilatero')
    elif (l1 == l2 and l2 != l3) or (l2 == l3 and l3 != l1) or (l1 == l3 and l3 != l2):
        print ('Triangulo Isociles')
    else:
        print ('Trinagulo Escaleno')
else:
    print('Não pode formar triangulo')
    