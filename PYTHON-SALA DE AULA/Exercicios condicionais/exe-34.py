nota1 = float ( input ( 'Primeira nota ?  ' ))
nota2 = float ( input ( 'Segunda  nota ?  ' ))
m = (nota1 + nota2 ) / 2

if ( m >= 7):
     print ( 'ALUNO OBTEVE NOTA >>> {}, ESTÁ APROVADO '.format(m))
elif (m <7):
   print ( 'ALUNO REPROVADO')
elif ( m == 10):
   print ('ALUNO APROVADO COM DISTINÇÃO')
