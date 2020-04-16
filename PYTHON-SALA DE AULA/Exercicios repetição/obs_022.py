n1 = int ( input ('Digite o número: '))
n2 = int ( input ('Outro número: '))

contador = 1
cociente = 1
while cociente < n1:
    cociente = n2 * contador 
    contador += 1

    if cociente == n1:
        print (cociente)
    
print (cociente)
    
 