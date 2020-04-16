n = int ( input ('Qual é número que deseja verificar ? '))
limite_inferior = int ( input ('Limite inferior: '))
limite_superior = int ( input ('Limite superior: '))

print (f'OS NÚMEROS MULTIPLOS DE {n} SÃO: ',end=' , ')
for i in range(limite_inferior, limite_superior + 1):
    if n % i == 0:
        print(i, end='')
        
print('fim')