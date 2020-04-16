
sal = int ( input ('Digite o salario >>> '))
hora = int ( input ('Horas trabalhadas >>> '))

print ('- Salário Bruto até R$ 900,00 (inclusive) - isento')
print ('- Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%')
print ('- Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%')
print ('- Salário Bruto acima de R$ 2.500,00 - desconto de 20%')
print ('='*43)      

salario = (sal * hora)
#DESCONTOS 
ir = ( salario * 0.05 )
inss = ( salario * 0.10 )
des =( ir + inss)

des1 = (salario * 0.95) 
des2 = (salario * 0.90)
des3 = (salario * 0.80) 
#ACRECIMOS 
fgts = ( salario * 0.11 )
#SALÁRIO LIQUIDO  
sal_liquido = ( salario - des ) + fgts

sal_liquido1 = ((salario * 0.95) - des) + fgts
sal_liquido2 = ((salario * 0.90) - des) + fgts
sal_liquido3 = ((salario * 0.80) - des ) + fgts

if ( sal <= 900 ):
      print ('-DESCONTO INSS > R${:.2f}'.format(inss))
      print ('-DESCONTO   IR > R${:.2f}'.format(ir))
      print ('-AUMENTO FGTS > R${:.2f}'.format(fgts))
      print ('='*43)      
      print ('( Insento de taxa de desconto )') 
      print ('-Salario Bruto: R${:.2f}'.format(salario))
      print ('-Salário liquido: R${:.2f}'.format(sal_liquido))
elif ( 900 < sal <= 1500  ) :
      print ('-DESCONTO INSS > R${:.2f}'.format(inss))
      print ('-DESCONTO   IR > R${:.2f}'.format(ir))
      print ('-AUMENTO FGTS > R${:.2f}'.format(fgts))
      print ('='*43)      
      print ('-( Desconto de 5% )')
      print ('-Salario Bruto: R${:.2f}'.format(salario))
      print ('-Salario Bruto com desconto de 5%: R${:.2f}'.format(des1))
      print ('-Salário liquido: R${:.2f}'.format(sal_liquido1))
elif ( 1500 < sal <= 2500 ):
      print ('-DESCONTO INSS > R${:.2f}'.format(inss))
      print ('-DESCONTO   IR > R${:.2f}'.format(ir))
      print ('-AUMENTO FGTS > R${:.2f}'.format(fgts))
      print ('='*43)      
      print ('-( Desconto de 10% )')
      print ('-Salario Bruto: R${:.2f}'.format(salario))
      print ('-Salario Bruto com desconto de 10%: R${:.2f}'.format(des2))
      print ('-Salário liquido: R${:.2f}'.format(sal_liquido2))
elif ( sal > 1500  ):
      print ('-DESCONTO INSS > R${:.2f}'.format(inss))
      print ('-DESCONTO   IR > R${:.2f}'.format(ir))
      print ('-AUMENTO FGTS > R${:.2f}'.format(fgts))
      print ('='*43)      
      print ('-( Desconto de 20% )')
      print ('-Salario Bruto: R${:.2f}'.format(salario))
      print ('-Salario Bruto com desconto de 20%: R${:.2f}'.format(des3))
      print ('-Salário liquido: R${:.2f}'.format(sal_liquido3)) 
