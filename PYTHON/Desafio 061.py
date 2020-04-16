primeiro = int(input('Primero termo: '))
razão = int ( input ('Razão: '))

cont = 1
s = primeiro

print(f'{s}', end=' -> ')
while cont < 10:
    razão += primeiro 
    print (razão, end=' -> ')
    cont += 1
print ('FIM!')