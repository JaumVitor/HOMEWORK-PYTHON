num = int ( input ('Número ? '))

n1 = num // 1000
n2 = ( num % 1000 ) // 100
n3 = ( num % 100 ) // 10 
n4 = ( num % 10 ) % 10

d1 = ( n1 * 10 ) + ( n2 * 1 )
d2 = (n3 * 10 ) + ( n4 * 1 )
soma = (d1 + d2 )
elv=  ( soma ** 2)

print ('O NÚMERO {}, DIVIDIDO AO MEIO CORRESPONDE AO {} e {} '.format(num,d1,d2))
print ('A SOMA ENTRE OS DOIS NOVOS NUMEROS É >>> {}'.format( soma))
print ('A SOMA AO QUADRADO CORRESPONDE AO {}'.format( soma ** 2 ))

if (elv == num):
   print ('Os números são iguais')
else :
   print ( 'Os númeos não são iguais')




