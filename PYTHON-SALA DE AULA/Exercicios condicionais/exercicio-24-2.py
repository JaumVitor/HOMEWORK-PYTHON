print (' CATEGORIA\n1. LIMPEZA\n2. ALIMENTAÇÃO\n3. VESTUÁRIO\nSituação pode ser [R ou N]','\n')

pre = float ( input ('Qual o preço ? '))
cat = int ( input ('Qual a categoria ? '))
sit = str ( input ('Qual a situação ? '))

if ( pre <= 25 ) &( cat == 1 ):
	aumento = pre * 1.05
	print (' Aumento de 5%, R${:.2f}'.format(pre * 1.05))
elif ( pre <= 25 ) & ( cat == 2 ):
	aumento = pre * 1.08
	print (' Aumento de 8%, R${:.2f}'.format(pre * 1.08))
elif ( pre <= 25 ) & ( cat == 3):
	aumento = pre * 1.10
	print (' Aumento de 10%, R${:.2f}'.format(pre * 1.10))

elif ( pre > 25 ) & ( cat == 1):
	aumento = pre * 1.18
	print (' Aumento de 12%, R${:.2f}'.format(pre * 1.18))
elif ( pre > 25 ) & ( cat == 2 ): 
	aumento = pre * 1.15
	print ( 'Aumento de 15%, R${:.2f}'.format(pre * 1.15))
elif ( pre > 25 ) & ( cat == 3 ):
	aumento = pre * 1.18
	print ( 'Aumento de 18%, R${:.2f}'.format(pre * 1.18))

if ( sit == 'R') or ( sit == 'r') and ( cat == 2 ):
	imposto = ( pre * 0.05 )
elif (sit == 'N') or ( sit == 'n' ) :
	imposto = ( pre * 0.08 )
else :
                imposto = ( pre * 0.08 )
               
novo = aumento - imposto 

print ('O novo preço, R${:.2f}'.format(novo))
if ( novo <= 50):
   print ('Está preço é classificado entre os baratos ')
elif ( 50 < novo <= 120 ):
   print ('Este preço é classificado entre os normais ')
elif ( 120 < novo ):
   print ('Este preço está classificado entre os caros ')
