sal = float ( input ('Qual valor do salário ? '))
if ( sal <= 300 ):
      nsal1 = (sal * 1.65) 
      print ('Salário com aumento de 35%: R${}'.format(nsal1))
elif( sal > 300):
      nsal2 = ( sal * 1.85)
      print ( 'Salário com aumento de 15%: R${}'.format(nsal2))
