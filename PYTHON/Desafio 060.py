# num = int ( input('Digite o número: '))       PRIMEIRA FORMA DE RESOUÇÃO 

# print ('{}! = {}'.format(num, num),end='')
# for x in range (num - 1, 0, - 1 ):
#     fatorial = num * x
#     num = fatorial  
#     print(' x {}'.format(x), end='')
# print(' = {}'.format(num))

# num = int ( input ('Digite o número: '))       SEGUNDA FORMA DE RESOLUÇÃO 

# c = num 
# f = 1

# while c > 0:
#     f = f * c

#     print(f'{c}', end='')
#     if c > 1:
#         print(' x ', end='')
#     else:
#         print(' = ', end='')

#     c -= 1

# print (f)

from math import factorial
num = int(input('Digite o número: '))

cont = num 
while cont > 0:
    print (f'{cont}', end = '')
    print (' x ' if cont > 1 else ' = ', end ='' )
    cont -= 1 

print (f'{factorial(num)}')