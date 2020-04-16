print ('=' *50)
nota1 = float ( input ('A primeira nota ? '))
nota2 = float ( input ('A segunda nota ? '))
print ('=' * 50)
#############################################################
media  = ( nota1 + nota2 ) / 2
#############################################################
if (  10 >= media >= 7 ):
      print ('Aprovado com média {} '.format(media))
elif (4 < media < 7):
      print ('Exame com média {}'.format(media))
elif ( 0 <= media <= 4):
      print ('Reprovado com média {}'.format(media))


