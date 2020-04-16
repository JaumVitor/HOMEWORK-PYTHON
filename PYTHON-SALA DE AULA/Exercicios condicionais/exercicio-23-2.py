cod = int ( input ('Codigo da compra ? ')) 
q = int ( input ('Quantidade de produtos ? '))

if (  1 <= cod <= 10 ):
	pro = 10

elif ( 11 <= cod <= 20 ):
	pro = 15

elif ( 21 <= cod <= 30 ):
	pro = 20

elif ( 31 <= cod <= 40 ):
	pro = 30

valor = pro * q 

if ( valor <= 250):
	print ('* Preço umitário > {}'.format(pro))
	print ('* Preço total da compra > R${}'.format(valor))
	print ('* Valor irá receber desconto de 5% > {}'.format(valor * 0.95))
elif ( 250 < valor <= 500 ):
	print ('* Preço umitário >{}'.format(pro))
	print ('* Preço total da compra > R${}'.format(valor))
	print ('Valor irá receber desconto de 10% > {} '.format(valor * 0.90))
elif ( 500 < valor ):
	print ('* Preço umitário > {}'.format(pro))
	print ('* Preço total da compra > R${}'.format(valor))
	print ('* Valor irá receber desconto de 15% > {}'.format(valor * 0.85))

