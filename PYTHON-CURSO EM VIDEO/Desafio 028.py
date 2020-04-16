from random import randint
from time import sleep

print ('=--='*15)
print ('vamos brincar.... escolha um número que esteja entre entre 0 e 5 e tente sua sorte!'.upper())
print ('=--='*15)

pc = randint(0,5)
n = int ( input ('Digite o valor e veja se acertou meu número HEHE ?'))
print ('AGUARDE....')
sleep(3)
if ( n == pc ):
      print ('PARÁBENS mizeravel ! vc acertou meu número urrh! ')
else:
      print ('HAHAH ERROU ! Eu pensei no {} e vc no {}'.format(pc , n))
