print ('- salários até R$ 280,00 (incluindo) : aumento de 20%')
print ('- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%')
print ('- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%')
print ('-salários de R$ 1.500,00 em diante : aumento de 5%')
print ('='*43)
sal = float ( input ('Qual valor do salario ? '))

if (sal <= 280 ):
	nsal1 = ( sal * 1.20 )
	print ('='*43)
	print ('-Aumento de 20 %') 
	print ('-Salario antigo : R${:.2f}'.format(sal))
	print ('-Novo salario é R${:.2f}'.format(nsal1)) 
elif (sal > 280 ) and ( sal <= 700 ):
	nsal2 = ( sal * 1.15 )
	print ('='*43)
	print ('-Aumento de 15 %') 
	print ('-Salario antigo : R${:.2f}'.format(sal))
	print ('-Novo salario é R${:.2f}'.format(nsal2))
elif (sal > 750 ) and ( sal <= 1500 ):
	nsal3 = ( sal * 1.10 )
	print ('='*43)
	print ('-Aumento de 10 %') 
	print ('-Salario antigo : R${:.2f}'.format(sal)) 
	print ('-Novo salario é R${:.2f}'.format(nsal3))
elif (sal > 1500 ):
	nsal4 = ( sal * 1.5 )
	print ('='*43)
	print ('-Aumento de 5%') 
	print ('-Salario antigo : R${:.2f}'.format(sal))
	print ('-Novo salario é R${:.2f}'.format(nsal4))
