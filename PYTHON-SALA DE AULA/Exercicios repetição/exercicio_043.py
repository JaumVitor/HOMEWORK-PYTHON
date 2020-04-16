n = int ( input ('Infome quantos números: '))

soma = 0
quantidade = 0 
for i in range (1, n + 1 ):
    num = float ( input (f'Digite o {i}° número para saber a média: '))
    soma += num
    quantidade += 1 
media = soma / quantidade

print (f'A media dos números informados é > {media:.1f}')