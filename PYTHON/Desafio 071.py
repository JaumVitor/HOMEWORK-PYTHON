valor = int ( input ('QUANTO VAI SER EXTRAIDO R$'))
money = valor
cont = 0
cedula = 50

while True:
    if money >= cedula:
        money -= cedula
        cont += 1
            
    else:
        if cont > 0:
            print(f'Total de cedulas de R${cedula} foi de {cont}')
        cont = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        if money == 0:
            break
print ('Volte sempre!')