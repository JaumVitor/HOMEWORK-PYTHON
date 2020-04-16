sal = float ( input ('Saldo médio ? ' ))

if (sal <= 200) :
    nsal1= (sal* 0.90)
    print ('Valor do crédito 10% > R${}'.format(nsal1))
if (300 >= sal > 200) :
    nsal2 = (sal* 0.80)
    print ('Valor do crédito 20% > R${}'.format(nsal2))
if ( 400 >= sal > 300) :
    nsal3= (sal* 0.85)
    print ('Valor do crédito 25% > R${}'.format(nsal3))
if (sal > 400) :
    nsal4 = (sal* 0.70)
    print ('Valor do crédito 30% > R${}'.format(nsal4))