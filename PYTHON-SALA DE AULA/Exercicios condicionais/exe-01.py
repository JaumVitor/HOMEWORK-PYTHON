a = float(input('Primeiro valor = '))
b = float(input(' Segundo valor = '))
c = float(input(' Teceiro valor = '))
if (a == b) and (b == c):
   print('Todos os valores são iguais')
elif (a == b) or (b == c) or ( a == c):
   print('Dois valores são iguais')
elif (a != b) and (a != b) and (c != b):
   print('Todos são difenrentes')
