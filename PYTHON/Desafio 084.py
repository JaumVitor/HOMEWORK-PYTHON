pessoa = list()
galera = list()
quantidade = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))

    if len(galera) == 0:
        maior = pessoa[1]
        menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        else:
            menor = pessoa[1]

    galera.append(pessoa[:])
    pessoa.clear()

    while True:
        finalizar = str (input ('Quer continuar ? ')).upper()[0]
        if finalizar in 'NS':
            break
    if finalizar in 'N':
        break

for individuo in range(len(galera)):
    if galera[individuo][0] not in '':
        quantidade += 1   #Pecorrendo para saber a quantidade de pessoas //Seria mais didatico eu usar len(galera)

print (f'Ao todo temos {quantidade} pessoas cadastradas ')

print (f'O maior peso foi de {maior}Kg e a listagem de pessoas foi ',end='')
for p in galera:
    if p[1] == maior:
        print (f'[{p[0]}]'.upper(),end='')
print()

print (f'O menor peso foi de {menor}Kg e a listagem de pessoas foi ',end='')
for p in galera:
    if p[1] == menor:
        print (f'[{p[0]}]'.upper(),end='')
print()


        
