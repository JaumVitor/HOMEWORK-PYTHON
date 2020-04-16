n = input ('Digite algo a ser considerado [OBJETO]: ')

print ('CLASSE DO OBJETO ? ', type(n) )
print ('OBJETO TEM ESPAÇO [V/F] ?', n.isspace()) 
print ('OBJETO PODE SER CONCIDERADO UM NUMERO [V/F] ? ', n.isnumeric() )
print ('OBJETO PODE SER CONCIDERADO ALFABETO [V/F] ? ', n.isalpha() )
print ('OBJETO NUMERICO E ALFABETICO  [V/F] ? ', n.isalnum() )
print ('OBJETO TEM TODAS AS LETRAS MAIUSCULSAS [V/F] ? ', n.isupper() )
print ('OBJETO TEM TODAS AS LETRAS MINUSCULAS [V/F] ? ',n.islower () )
print ('OBJETO É CAPTALIZADO [V/F] ? ',n.istitle() )




