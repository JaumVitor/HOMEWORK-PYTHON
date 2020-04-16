n = int ( input ('Pretende somar ate que número ? '))

soma = 0
for i in range(1, n + 1):
    soma += i
    print (i,end='')

    if i < n:
        print( end=' + ')
    
    if i == n:
        print(' = ', end='')
print (soma)
