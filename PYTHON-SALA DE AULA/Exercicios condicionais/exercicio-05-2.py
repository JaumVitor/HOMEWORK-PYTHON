num1 = float ( input ('Digite o número ? '))
num2 = float ( input ('Digite outro número ? '))
tipo = int ( input ('Escolha 1,2,3 ou 4 ? '))

if ( tipo == 1 ):
   m = ( num1 + num2 ) / 2
   print ('Média é {}'.format(m))
elif ( tipo == 2) and ( num1 > num2 ):
   print ('Diferença >>> {:.0f}-{:.0f} = {:.0f}'.format(num1, num2, num1-num2))
elif ( tipo == 2) and ( num2 > num1):
   print ('Diferença >>> {:.0f}-{:.0f} = {:.0f}'.format(num2, num1, num2-num1))
elif ( tipo == 3):
   print ('Produto >>> {:.0f}×{:.0f} = {}'.format(num1, num2, num1*num2)) 
elif ( tipo == 4):
   print ('Divisão >>> {:.0f}÷{:.0f} = {:.2f}'.format(num1, num2, num1/num2))
