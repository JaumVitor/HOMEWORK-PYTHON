lista = list()

while True:
    lista.append(int (input ('Declare o número: ')))
    while True:
        fim = str (input ('Deseja continuar ? '.upper())).upper()[0]
        if fim in 'SN':
            break
    if fim in 'N':
        break

lista.sort(reverse=True)        #Reverter os valores ordenados dentro da lista

print (f'\nNa lista temos {len(lista)} números')
print(f'Os valores da sua lista são: {lista}')
if 5 in lista:
    print ('O valor 5 esta dentro da lista!')
else:
    print ('O valor 5 NÃO esta dentro da lista!')
