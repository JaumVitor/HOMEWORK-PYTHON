limite_inferior = int(input('INFORME ONDE IRÁ COMEÇAR:  '))
limite_superior = int(input('INFORME O LIMITE SUPERIOR: '))

for i in range(limite_inferior, limite_superior + 1):
    if i % 2 != 0:
        print(i)
