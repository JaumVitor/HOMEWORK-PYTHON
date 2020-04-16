print ('Até 5 Kg Acima de 5 Kg \nMorango R$ 2,50 por Kg R$ 2,20 por Kg \nMaçã R$ 1,80 por Kg R$ 1,50 por Kg')
print ('')
kgma = float  ( input ('Quantidade em kg de Maçãs ? '))
kgmo = float  ( input ( 'Quantidade em kg de Morangos ?'))

if ( kgmo <= 5 ) or ( kgma <= 5 ):
      preço1 = ( kgma * 1.80 )
      preço2 = ( kgmo * 2.50 )
      valor12 = ( preço1 + preço2 )
      print ('--' * 42)
      print ( 'O valor a ser gasto com as Maçãs R${}'.format(preço1))
      print ( 'O valor a ser gato com os Morangos R${}'.format(preço2))
      print ('--' * 42)
      print ( 'VALOR TOTAL A SER GASTO É >>> R${}'.format(valor12))
      print ('=' * 47)
elif ( kgmo >  5 ) or ( kgma > 5 ):
      preço3 = ( kgma * 1.50 )
      preço4 = ( kgmo * 2.20 )
      valor34 = ( preço3 + preço4 )
      print ('--' * 42)
      print ( 'O valor a ser gasto com as Maçãs R${:.2f}'.format(preço3))
      print ( 'O valor a ser gato com os Morangos R${:.2f}'.format(preço4))
      print ('--' * 42)
      print ( 'VALOR TOTAL A SER GASTO É >>> R${:.2f}'.format(valor34))
      print ('=' * 47)
if ( kgma + kgmo >= 8 ) and ( kgmo > 5 ) or ( kgma > 5 ):
      new1 = ( valor34 * 0.9 )
      print ( ' VALOR COM DESCONTO DE 10% >>> {}'.format(new1))
elif ( kgma + kgmo >=8 ) and ( kgmo <= 5 ) or ( kgma <= 5 ) :
      new2 = ( valor12 * 0.9)
      print ( ' VALOR COM DESCONTO DE 10% >>> {}'.format(new2))

