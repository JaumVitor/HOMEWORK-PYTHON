num = int ( input ("Número de 2 digitos ? "))
dez = ( num // 10) 
uni = ( num % 10)

if (dez == uni) :
    print ("Dezena = unidade" ) 
elif (dez != uni) :
    print ("Dezena é diferente da unidade") 
