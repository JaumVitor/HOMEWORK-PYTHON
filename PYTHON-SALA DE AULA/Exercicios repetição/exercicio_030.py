desconto = ''
end = True
preço_produto = novo = 0

while end:
    produto = str ( input ('Qual nome do produto ? ')).upper().strip()
    if produto == 'FIM':
        break
    
    preço = float ( input ('Preço do produto R$ '))
    quantidade = int ( input ('Quantos produtos foram comprados ? '))

    if quantidade <= 10:
        novo = preço
        desconto = '0%'
    elif 10 < quantidade <= 20:
        novo = preço * 0.90
        desconto = '10%'
    elif 20 < quantidade <= 50:
        novo = preço * 0.80
        desconto = '20%'
    elif 50 < quantidade:
        novo = preço * 0.75
        desconto = '25%'
    
    preço_produto = novo * quantidade
    
    print(
        f'''
°°°°°°°°°°°°°°°°°°°°LISTA DE COMPRAS:°°°°°°°°°°°°°°°°°°°°°°

Total de {quantidade} {produto} - - - - - R${preço_produto}
DESCONTO - {desconto} Agradecemos a visita, volte sempre!
''')
    
