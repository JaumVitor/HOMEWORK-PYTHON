from time import sleep

vel = float ( input ('Qual a velocidade que vc estava dirigindo ?'))
print ('Agurde um momento....estamos análisando sua velocidade ;)')
sleep(3)

if vel > 80 :
  multa = ( vel - 80 ) * 7
  print ('Calma rapaizinho... vc foi multado ! Sua multa terá o valor de R${}'.format(multa))
else:
  print ('Muito bem garoto, tenha um bom dia !....está andando de acordo com o padrão!')
        