stop = 'S'
cont = soma = maior = menor = 0

while stop in 'Ss': 
    valor = int ( input ('Digite o valor : '))
    stop = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]

    cont += 1
    soma += valor
    
    if cont == 1:
        maior = valor
        menor = valor
    else: 
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
         
media = soma / cont
print (f'Você digitou {cont} números')
print (f'A media dos valores é {media}','\n',f'O maior valor é {maior} e o menor é {menor}')



