print ('='*40, '\nESCREVA UM NÚMERO DE 4 DIGITOS')
print ('=' *40)
num = int ( input ('Número ? ' ))

dez1 = (num // 100) #variaveis 
dez2 = (num % 100) #variaveis 
raiz = num **(1/2) #variaveis 

if ( raiz == dez1 + dez2 ):
    print ('-' *40)
    print ('ESSE NÚMERO É UM QUADRADO PERFEITO! :) ') 
else :
    print ('-' *40)
    print ('ESSE NÚMERO NÃO É UM QUADRADO PERFEITO! :( ' ) 

