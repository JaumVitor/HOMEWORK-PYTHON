def area(larg, comp):		#Função que calcula área 
	a = larg * comp
	print (f'A área do terreno de {larg}x{comp} é {a}m²')

print ('CALCULO DA ÁREA:')
l = float (input ('largura (m): '))
c = float (input ('Comprimento (m): '))
print ()

area(l,c)