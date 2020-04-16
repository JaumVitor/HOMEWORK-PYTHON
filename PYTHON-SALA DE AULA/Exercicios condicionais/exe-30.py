litro = float ( input ( 'Quantos litros foram vendidos ? '))
tipo = str ( input ( 'Gasolina ou Alcool [G/A] ? '))
print ('='*40)

if ( litro <= 20 ) and (( tipo == 'a' ) or ( tipo == 'A' )):
    apreço1 = ( litro * 1.90) * 0.97 
    print ('Cliente escolhendo Alcool (Com desconto de 3%)\n> Preço final é R${:.2f}'.format(apreço1))
elif ( litro > 20 ) and (( tipo == 'a' ) or ( tipo == 'A' )):
    apreço2 = ( litro * 1.90) * 0.95
    print ('Cliente escolhendo Alcool (Com desconto de 5%)\n> Preço final é R${:.2f}'.format(apreço2))

elif ( litro <= 20 ) and ( tipo == 'g' ) or ( tipo == 'G'):
    gpreço1 = (litro * 2.50 ) * 0.96
    print ('Cliente escolhendo Gasolina (Com desconto de 4%)\n> Preço final é R${:.2f}'.format(gpreço1))
elif ( litro > 20 ) and ( tipo == 'g') or ( tipo == 'G'):
      gpreço2 = (litro * 2.50) * 0.94 
      print ( 'Cliente escolhendo Gasolina (com desconto de 6%)\n>Preço final é R${:.2f}'.format(gpreço2))
