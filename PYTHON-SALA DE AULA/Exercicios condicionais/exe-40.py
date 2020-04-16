p1 = str ( input ( 'Telefonou pra vítima ? '))
p2 = str ( input ( 'Esteve no local do crime ? '))
p3 = str ( input ( 'Mora perto da vítima ? '))
p4 = str ( input ( 'Devia para a vítima ? '))
p5 = str ( input ( 'Já trabalhou com a vítima ? '))

if ( p1 == 's') or ( p1 == 'S') :
      per1 = 1
else :
      per1 = 0
#################################
if ( p2 == 's') or ( p2 == 'S') :
      per2 = 1
else :
      per2 = 0
#################################
if ( p3 == 's') or ( p3 == 'S') :
      per3 = 1
else :
      per3 = 0
#################################
if ( p4 == 's') or ( p4 == 'S') :
      per4 = 1
else :
      per4 = 0
#################################
if ( p5 == 's') or ( p5 == 'S') :
      per5 = 1
else :
      per5 = 0
#################################
soma = per1 + per2 + per3 + per4 + per5 

if ( soma == 2 ):
      print ('='*40)
      print ('O sujeito é Suspeito')
      print ('='*40)
elif ( 5 > soma > 2 ):
      print ('='*40)
      print ('O sujeito é Cumplice')
      print ('='*40)
elif ( soma == 5 ):
      print ('='*40)
      print ('O sujeito é Assacino ')
      print ('='*40)
else :
      print ('='*40)
      print ('O sujeito é Inocente')
      print ('='*40)


















