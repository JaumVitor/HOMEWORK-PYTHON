print ('----------Até 5 Kg----------\n[1] File       > R$ 4,90 por Kg')
print ('[2] Alcatra  > R$ 5,90 por Kg')
print ('[3] Picanha > R$ 5,90 por Kg\n')
print ('-------Acima de 5 Kg-------\n[1] File       > R$ 5,80 por Kg')
print ('[2] Alcatra  > R$ R$ 6,80 por Kg')
print ('[3] Picanha > R$ 7,80 por Kg\n')
print ('ACEITAMOS CARTÃO >>> TABAJÁRA COM ATÉ 5% DE DESCONTO\n')

tipo  = int ( input ( 'Tipo de carne ? '))
kg = float ( input ( 'Quantidade de carne em kg ? '))
pag = str ( input ( ' Vai usar cartão Tabájara (S/N) ? '))

if ( tipo == 1 ) and ( kg <= 5) and (( pag == 's' ) or ( pag == 'S')):
   valor = ( kg * 5.90 )
   desc1 = ( preço1 * 0.05 ) 
   desc = ( preço1 * 0.95 )
 
   print ('--' * 42)
   print ( '> Quantidade de carne {}'.format(kg))
   print ( '> O valor total a ser gasto com R${}'.format(valor))
   print ( '> Desconto de R${}'.format(desc1))
   print ( '> VALOR FINAL >>> R${}'.format(desc))
   print ('--' * 42)

elif  ( tipo == 1 ) and ( kg <= 5) and (( pag == 'n' ) or ( pag == 'N')):
   valor = ( kg * 5.90 )
   desc1 = ( preço1 * 0.05 ) 
   desc = ( preço1 * 0.95 )
 
