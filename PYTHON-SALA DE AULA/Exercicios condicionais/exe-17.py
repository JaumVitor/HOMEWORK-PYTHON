print ('=' *40)
ang = int ( input ('Angulo ? ')) 
print ('=' *40) 

if (ang > 0)and (ang <= 90):
    print ('{}° Corresponde ao 1° quadrante'.format(ang))
elif (ang > 90) and (ang <= 180):
    print ('{}° Corresponde ao 2° quadrante'.format(ang))
elif (ang > 180) and (ang <= 270):
    print ('{}° Corresponde ao 3° quadrante'.format(ang))
elif (ang > 270) and (ang <= 360):
    print ('{}° Corresponde ao 4°quadrante'.format(ang)) 
elif (ang > 360):
    print ('É NECESSÁRIO REDUZIR AO PRIMEIRO QUADRANTE') 
print ('=' *40)