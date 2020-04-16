# n = int ( input ('Informe o número para ser indicado o seu fatorial: '))

# fatorial = 1
# print(n, '! = ', end='')
# for i in range(n, 0, -1):
#     fatorial *= i
# print (fatorial) 

n = int(input('Informe o número para ser indicado o seu fatorial: '))

i = n
fatorial = 1 
while i >= 1:
    fatorial *= i
    i -= 1
    print (fatorial)