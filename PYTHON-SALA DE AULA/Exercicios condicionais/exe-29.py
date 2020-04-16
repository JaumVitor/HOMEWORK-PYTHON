print ('='*50,'\nESCREVA UM NÚMERO DE 3 DIGITOS (MENOR QUE 1000)')
num = int ( input ( 'Número ? '))
print ('='*50)

cen = num // 100
dez = (num % 100) // 10
uni = (num % 10) % 10

print ( '{} >>> {} centenas, {} dezenas, {} unidades  '.format(num, cen, dez, uni ))
