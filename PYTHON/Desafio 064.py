print('Quando quiser parar digite o número [999]')

soma = 0
cont = 0
n = 0
saida = True

while saida:
    n = float ( input ('Digite o número: '))
    if n == 999:
        saida = False         
    else:
        soma += n 
        cont += 1
media = soma / cont 
print (f'A media dos números digitados é {media} e a soma = {soma}')

