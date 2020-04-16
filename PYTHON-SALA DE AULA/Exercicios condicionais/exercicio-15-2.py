tipo = int ( input ('Qual tipo de polpança ? '))
valor = float ( input ('Quanto quer reservar R$'))

if ( tipo == 1 ):
	valor1 = (valor * 0.03) 
	print ('Redimento mensal é R${}'.format(valor1))
elif ( tipo == 2 ):
	valor1 = (valor * 0.04)
	print ('Rendimento mensal é R${}'.format(valor1))
