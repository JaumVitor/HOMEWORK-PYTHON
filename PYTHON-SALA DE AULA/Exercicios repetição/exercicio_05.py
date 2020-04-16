x = int ( input ('Informe o valor x: '))
n = int ( input ('Infome o valor n: '))

resultado = 999
while resultado > 2:
    resultado = x // n
    print(resultado)
    x = resultado
    n += 1




