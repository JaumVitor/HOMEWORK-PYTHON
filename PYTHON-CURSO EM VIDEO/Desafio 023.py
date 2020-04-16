num = int ( input ('Número entre 0 e 9999 ? '))

n1 = num // 1000
n2 = ( num % 1000 ) // 100
n3 = ( num % 100 ) // 10
n4 =  ( num % 100 ) % 10

lista = [n1, n2, n3, n4]
print ('Milhares : {}'.format (lista[0]))
print ('Centenas : {}'.format (lista[1]))
print ('Desenas : {}'.format(lista[2]))
print ('Unidades : {}'.format(lista[3]))
