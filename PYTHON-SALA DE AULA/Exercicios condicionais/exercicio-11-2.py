sal = float ( input ('Salário ? ' ))

if (sal > 900) :
    print ('insento de reajuste') 
    print ('Salário com aumento de 0% > R${}'.format(sal))
elif (900 >= sal > 600) :
    nsal1 = (sal* 1.05)
    print ('Salário com aumento de 5% > R${}'.format(nsal1))
elif (600 >= sal > 300) :
    nsal2= (sal* 1.10)
    print ('Salário com aumento de 10% > R${}'.format(nsal2))
elif (sal <= 300):
    nsal3 = (sal* 1.15)
    print ('Salário com aumento de 15% > R${:.2f}'.format(nsal3))