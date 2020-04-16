limite_inferior = int ( input ('Digite o número de inicio: '))
limite_superior = int ( input ('Informe o limite: '))

for i in range (limite_inferior, limite_superior + 1 ):
    cont = 0 
    for x in range (limite_inferior, limite_superior + 1):
        if i % x == 0:
            cont += 1
    if cont <= 2:
        print(i)


