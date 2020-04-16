h_extra = float ( input ('Digite horas trabalhadas: '))
h_falta = float ( input ('Digite horas faltadas: '))

h = h_extra - (2/3 * (h_falta)) 
hd = h * 60

if ( 2400 < hd  ):
	premio = 500
	print (premio)
elif ( 1800 < hd <= 2400):
	premio = 400
	print (premio)
elif ( 1200 < hd <= 1800 ):
	premio = 300
	print (premio)
elif ( 600 < hd <= 1200):
	premio = 200
	print (premio)
elif ( hd <= 600 ):
	premio = 100
	print (premio)
