n1 = int ( input ('Digite o primeiro número: '))
n2 = int ( input ('Digite o segundo número: '))

div = 2
resultado = 1

if n1 == 0 or n2 == 0:
    resultado = 0
else:
    while n1 + n2 != 2:
        if (n1 % div) == 0 or (n2 % div) == 0:
            resultado = resultado * div 
            if n1 % div == 0:
                n1 = n1 // div
            if n2 % div == 0:
                n2 = n2 // div
        else:
            div += 1  
print (f'O Minimo multiplo comum entre os números é {resultado} ')
     