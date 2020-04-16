sal = float ( input ('Qual o salário bruto do trabalhador ? '))

if ( sal <= 350 ):
	nsal = sal * 0.93
	salb = nsal + 100
	print ( 'Salário deve ter uma gratificação de R$100\nPorém tem uma redução de 7% (impostos)>>> Salário liquido será R${}'.format(salb))
elif ( 350 < sal <= 600 ):
	nsal = sal * 0.93
	salb = nsal + 75
	print ( 'Salário deve ter uma gratificação de R$75\nPorém tem uma redução de 7% (impostos)>>> Salário liquido será R${}'.format(salb))
elif ( 600 < sal <= 900 ):
	nsal = sal * 0.93
	salb = nsal + 50
	print ( 'Salário deve ter uma gratificação de R$50\nPorém tem uma redução de 7% (impostos)>>> Salário liquido será R${}'.format(salb))
elif ( 900 < sal ):
	nsal = sal * 0.93
	salb = nsal + 35
	print ( 'Salário deve ter uma gratificação de R$35\nPorém tem uma redução de 7% (impostos)>>> Salário liquido será R${}'.format(salb))
