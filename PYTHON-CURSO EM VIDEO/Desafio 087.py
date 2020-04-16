matriz = [[],[],[]]
soma_par = soma_coluna = 0

for linha in range(3):
    for coluna in range(3):
        indice = int(input(f'Digite o valor [{linha}|{coluna}]: '))
        matriz[linha].append(indice)
print ()

for m in matriz:
    for c in range(3):
        print(f'[{m[c]:^5}]', end='')
    print ()

for p in matriz:            #A) Soma dos números pares 
    for x in range(3):
        if p[x] % 2 == 0:
            soma_par += p[x]

for c in matriz:            #B) Soma dos valores da coluna 3 
    soma_coluna += c[2]

for i in range (len(matriz[1])):    #C) Calcular o maior valor da linha 2 
    if i == 0:
        maior = matriz[1][i]
    else:
        if matriz[1][i] > maior:
            maior = matriz[1][i]
print ()

print (f'A) Soma dos números pares foi de: {soma_par}')
print(f'B) Soma dos números da coluna 3 é de: {soma_coluna }')
print (f'C) O maior valor da linha 2 foi o número: {maior}')