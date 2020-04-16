n = int ( input ('Qual o ultimo número inteiro ? '))

for i in range (1, n + 1):
    print(i,end='')
    
    if i != n:
        print(' , ',end='')
    else:
        print ('...FIM')