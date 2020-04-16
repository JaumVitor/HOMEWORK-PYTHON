pre = float ( input ('Qual preço R$'))

if (pre <=30 ):
	print ('Valor isento de desconto, R${}'.format(pre))
elif ( 30 < pre <= 100 ):
	des = ( pre * 0.90)
	print ('Valor com desconto de 10%, R${}'.format(des))
elif ( 100 < pre ):
	des = ( pre * 0.85)
	print ('Valor com desconto de 15%, R${}'.format(des))
