sal = float ( input ('Digite valor do salário ? '))
if ( sal < 500 ):
   nsal = ( sal * 1.65 ) 
   print (' reajuste salárial de 30% : R${}'.format(nsal))
else :
      print ( 'salario não merece um reajuste....então permanece o mesmo' )
