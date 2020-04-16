n = int ( input ('Qual número será usado como aproximação ? '))

for i in range(1, n + 1):
    raiz = i * i

    if raiz > n:
        break
        
    print(raiz)
