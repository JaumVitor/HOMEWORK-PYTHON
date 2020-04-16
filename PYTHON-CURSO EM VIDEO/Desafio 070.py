
preço = quant = soma_preço = quant_mil = cont = 0
produto = ' '
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço R$'))
    cont += 1

    if cont == 1:    #if cont == 1 or preço < barato:   com isso elimino 
        barato = preço
        menor_produto = produto
    elif preço < barato:                               # Sai Caso eu tivesse colocado o de cima 
        barato = preço                                 # Sai - - - - - - - - - - - - - - - - - 
        menor_produto = produto                        # Sai - - - - - - - - - - - - - - - - - 
        
    if preço > 1000:
        quant_mil += 1          #Quantidade de produtos com valor acima de 1.000 
        
    soma_preço += preço         #Soma de todos os preços de produtos 
    
    c = ' '
    while c not in 'SN':
        c = str(input('Ainda quer analisar ? ')).strip().upper()[0]
        print ('')
    if c in 'N':
        break

print(
    '{:-^40}'.format('LISTA DE COMPRAS'))
print(
    f'O valor total gasto na compra foi R${soma_preço}')
print(
    f'O produto mais barato foi > {menor_produto} e seu valor é de R${barato}')
print(
    f'Temos {quant_mil} produtos que custam mais de R$1.000')