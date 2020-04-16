cat1 = int ( input ( 'Qual cateto oposto ? '))
cat2 = int ( input ( 'Qual o cateto adjacente ?'))

r = ( cat1 ** 2 ) + ( cat2 ** 2 )
hipo = ( r ** 0.5 )
print ( 'Cateto oposto > {}'.format( cat1 ))
print ( 'Cateto adjacente > {}'.format( cat2 ))
print ( 'hipotenusa > {} '.format ( hipo ) )
