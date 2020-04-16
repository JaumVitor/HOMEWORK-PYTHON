n = int (input('Informe o triangular : '))

cont, n2, n3 = 1, 2, 3  #Váriaveis 
'''
Porderia muito bem utilizar somente uma variavel 'i' por exemplo. Neste caso eu deixaria: 
i = 1 
while i * (i + 1) * (i + 2)
	cod cod cod cod 
	i += 1 
conpreendeu ? se não assista a aula curso de python Youtube de nº 15
'''
while True:
	var = cont * n2 * n3
	print(f'{cont} x {n2} x {n3} = {var} ')
	
	if var >= n:
		break

	cont += 1
	n2 += 1
	n3 += 1

if var == n:
	print (f'Número {n} é um valor triangular! ')
else:
	print (f'O Número {n} não é um valor triangular! ')