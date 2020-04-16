idade = int ( input ('Qual a idade do paciente ? '))
peso = float ( input ('Qual o peso do paciente ? '))

if  ( idade <= 20  ) and ( 90 < peso ):
	print ('Risco 7')
elif ( idade <= 20 ) and ( 60 < peso <= 90 ):
	print ('Risco 8') 
elif  ( idade <= 20 ) and ( peso <= 60):
	print ('Risco 9')

elif ( 20 < idade <= 50 ) and ( 90 < peso ):
	print ('Risco 4')
elif ( 20 < idade <= 50 ) and ( 60 < peso <= 90 ):
	print ('Risco 5')
elif ( 20 < idade <= 50 ) and ( peso <= 60):
	print ('Risco 6')

elif ( 50 < idade ) and ( 90 < peso ):
	print ('Risco 1')
elif ( 50 < idade ) and ( 60 < peso <= 90 ):
	print ('Risco 2')
elif ( 50 < idade ) and (  peso <= 60):
	print ('Risco 3')
