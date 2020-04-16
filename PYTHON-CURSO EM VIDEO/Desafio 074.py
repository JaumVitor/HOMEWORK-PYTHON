from random import randint

print ('Os números sortedos foram: ',end='')
for i in range(5):
    numeros = randint(0, 10)    #podieria ter usado as tuplas...numeros = (randint(1,10), randint(1,10)) DESSA MANEIRA AS VARIAVEIS SÃO ISOLADAS
                                    
    if i == 0:              #min(numeros), max(numeros)  pra dizer qual foi o maior e menor valor
        maior = numeros
        menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros

    print (numeros,end ='')
    if not i >= 4:
        print (', ', end ='') 

print ('\n')
print (f'O maior número entre os sorteados foi o {maior}.') 
print (f'Além disso, o menor número dos sorteados foi o {menor}.')
