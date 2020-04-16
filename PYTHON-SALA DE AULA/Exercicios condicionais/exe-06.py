ang1 = int ( input (" primeiro angulo ? " ))
ang2 = int ( input (" Segundo angulo ? " ))
ang3 = int ( input (" Terceiro angulo ? " ))

if (ang1 + ang2 +ang3 == 180):
    print ('Pode formar triângulo') 
    if (ang1 == 90) or (ang2 == 90) or ( ang3 == 90):
        print ('Triângulo Retângulo') 
    elif (ang1 < 90) and (ang2 < 90) and (ang3) :
        print ('Triângulo acutangulo') 
    elif (ang1 > 90) or (ang2 > 90) or (ang3 > 90):
        print ('Triângulo obrtusano') 
    

