pre = float ( input (' Qual valor do produto ? '))

if ( pre <= 50):
	produto = pre * 1.05
elif ( 50 < pre <= 100):
	produto = pre * 1.10
elif ( 100 < pre ):
	produto = pre * 1.15

if (produto <= 80):
	print ( 'Esse produto está classificado entre PREÇOS BARATOS!')
elif ( 80 < produto <= 120):
	print ('Esse produto está classificado entre PREÇOS NORMAIS!')
elif ( 120 < produto <= 200):
	print ('Esse produto está classificado entre PREÇOS CAROS!')
elif ( 200 < produto ):
	print ('Esse produto está classificado entre PREÇOS MUITO CAROS!')
