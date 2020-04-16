while True:
    n = int ( input ('Digite o valor da tabuada deseijada: '))

    if n < 0:
        break
        
    for i in range (1, 10): 
        print (f'{n} x {i} = {n * i}')
        
print ('Tabuada encerrada, volte sempre! ')
