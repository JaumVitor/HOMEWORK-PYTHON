anterior = 0
sucessor = 1
soma = 0
contador = 1  #Para saber quando for finalizar 

termo = int ( input ('Quantos termos de números fibonati ? '))
print ('0', end=' -> ')
while contador <= termo:
    print (sucessor, end =' -> ')
    soma = anterior + sucessor 
    anterior = sucessor  
    sucessor = soma
    
    contador += 1
print ('FIM')

# n1 = 0
# n2 = 1
# cont = 3

# print (f'{n1} -> {n2}', end=' -> ')

# x = int ( input ('Quantos números fibonacci ? '))
# while cont <= x:
#     n3 = n1 + n2 
#     print(f'{n3}', end=' -> ')
#     n1 = n2
#     n2 = n3 
    
#     cont += 1
# print ('FIM')

    