print ('=' *50)
nota1 = float ( input ('A primeira nota ? '))
nota2 = float ( input ('A segunda nota ? '))
print ('=' * 50)
#############################################################
media  = ( nota1 + nota2 ) / 2
#############################################################
if ( media >= 7 ):
      print ('ALUNO ESTÁ APROVADO [MÉDIA {}] '.format(media))
elif (media < 7):
      print (' COM ESSA NOTA, INFELIZMENTE O ALUNO ESTÁ REPROVADO! :( ')
      print ('--' * 42)



