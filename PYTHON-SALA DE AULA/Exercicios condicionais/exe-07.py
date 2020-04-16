l1 = int ( input (" primeiro lado ? " ))
l2 = int ( input (" Segundo lado ? " ))
l3= int ( input (" Terceiro lado ? " ))

if (l1 + l2) < l3 or (l2 + l3) < l1 or (l1 +l3) <l2:
    print ('Não pode formar triângulo ') 
elif (l1 + l2) > l3 or (l2 + l3) > l1 or (l1 +l3) > l2:
    print ('Pode formar triângulo') 
    if (l1 == l2 ) and ( l2 == l3 ):
        print ('Triângulo Isósceles ') 
    elif (l1 != l2 ) and ( l2 != l3):
        print ('Triângulo Escaleno') 
    elif ( l1 == l2 ) or (l1 == l3) or ( l3 == l2):
        print ('Triângulo Isósceles ')