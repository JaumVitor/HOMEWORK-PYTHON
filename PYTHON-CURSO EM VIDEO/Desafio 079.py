lista_número = list ()

while True:
    valor = int (input ('Digite o núemero: '))
    if valor not in lista_número:
        print ('Adicionado com sucesso!')
        lista_número.append(valor)
    else:
        print ('Valor não adicionado na lista!')

    while True:
        stop = str(input('Ainda quer continuar [S or N] ? '))[0].upper()
        print()

        if stop in 'NS':
            break
    if stop in 'N':
        break

lista_número.sort()
print ('Os valores adicionados na lista são: ',end=' ')

for n ,x in enumerate (lista_número):
    print(x,end='')
    if n + 1 < len(lista_número):
        print(',',end=' ')
    