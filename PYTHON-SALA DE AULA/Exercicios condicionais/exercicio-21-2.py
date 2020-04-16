print (' Leia o exercicio para saber o codigo de origem !')
pre = float ( input ('Digite preço do produto: ' ))
tipo = int ( input ('Codigo de origem ? '))

if (tipo == 1):
	print ('Preço do produto é R${}, [origem Sul] '.format(pre))
elif ( tipo == 2):
	print ( 'Preço do produto é R${}, [origem Norte]'.format(pre))
elif ( tipo == 3):
	print ( 'Preço do produto é R${}, [origem Leste]'.format(pre))
elif ( tipo == 4):
	print ( 'Preço do produto é R${}, [origem Oeste]'.format(pre))
elif ( tipo == 5) or ( tipo == 6) :
	print ( 'Preço do produto é R${}, [origem Nordeste]'.format(pre))
elif ( tipo == 7) or ( tipo == 8 ) or ( tipo == 9 ) :
	print ( 'Preço do produto é R${}, [origem Sudeste]'.format(pre))
elif (  9 < tipo < 21 ):
	print ( 'Preço do produto é R${}, [origem Centro-Oeste]'.format(pre))
elif (  20 < tipo < 31 ):
	print ( 'Preço do produto é R${}, [origem Noroeste]'.format(pre))
