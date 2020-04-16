matriz = [[],[],[]]

for linha in range (3):
    for casa in range (3):
        indice = int(input(f'Digite o Indice [{linha}|{casa}]:'))
        matriz[linha].append(indice)
print ()

for l in range (3):
    print (l,end=' ')
    for i in range(3):
        print(f'[{matriz[l][i]:^5}]',end='')
    print()
    
for x in range(3):
    print(f' {x:^6} ',end='')