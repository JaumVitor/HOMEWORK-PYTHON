import random

n1 = str ( input ( 'Nome 1 : '))
n2 = str ( input ('Nome 2 : '))
n3 = str ( input ('Nome 3 : '))
n4 = str ( input ('Nome 4 : '))
print ('=' * 15)

print ('{} é o número 1'.format ( n1 ))
print ('{} é o número 2'.format ( n2 ))
print ('{} é o número 3'.format ( n3 ))
print ('{} é o número 4'.format ( n4 ))

sort = random.randint(1,4)
print ('- ' *15 )

print ('O número sorteado é  {} '.format ( sort)) 
