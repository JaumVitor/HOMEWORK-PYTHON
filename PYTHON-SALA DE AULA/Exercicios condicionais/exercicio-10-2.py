valor = float ( input ( 'Qual valor de fabrica do carro ? '))

if ( valor <= 1200 ):
	imp = 0
	dis = valor * 0.05
	print ('IMPOSTO > {}\n%DISTRIBUIDOR > {}'.format(imp, dis))
	print ('Custo para o consumidor: R${}'.format(valor + imp + dis))
elif ( 25000 >= valor > 1200 ):
	imp = valor * 0.15 
	dis = valor * 0.10 
	print ('IMPOSTO > {}\n%DISTRIBUIDOR > {}'.format(imp, dis))
	print ('Custo para o consumidor: R${}'.format(valor + imp + dis))
elif ( valor > 25000 ):
	imp = valor * 0.20
	dis = valor * 0.15
	print ('IMPOSTO > {}\n%DISTRIBUIDOR > {}'.format(imp, dis))
	print ('Custo para o consumidor: R${}'.format(valor + imp + dis))
	
