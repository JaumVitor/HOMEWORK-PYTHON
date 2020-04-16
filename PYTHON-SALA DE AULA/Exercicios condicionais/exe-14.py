print ('=' *50)
nota1 = float ( input ('A primeira nota ? '))
nota2 = float ( input ('A segunda nota ? '))
print ('=' * 50)
#############################################################
media  = ( nota1 + nota2 ) / 2
#############################################################
if ( media >= 7 ):
      print ('O aluno obteve média de {} , e não ira para prova final '.format(media))
elif (media < 7):
      print ('O ALUNO ESTA DE RECUPERAÇÃO... ENTÃO É NECESSÁRIO OUTRA NOTA ! ')
      print ('--' * 42)
      nota3 = float ( input ('Nota da recuperação ? '))
      media2 = (media + nota3 ) / 2 
if  (  media2 >= 5 ):
      print ('ALUNO ESTÁ APROVADO ! :)')
else :
      print ('COM ESSA NOTA, INFELIZMENTE O ALUNO ESTÁ REPROVADO! :( ')


