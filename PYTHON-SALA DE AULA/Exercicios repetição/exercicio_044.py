x = int ( input ('Quantos números quer informar na lista ? '))

for i in range (1 , x + 1 ): 
    n = int ( input ('Digite o número: '))

    if i == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
print (f'O Maior número da lista foi o número {maior}\nO Menor número da lista foi o {menor} ')