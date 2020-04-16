print ('='*40)
print ('MEDIA NECESSÁRIA PARA SER APROVADO')
print ('='*40)
print ('Entre 9.0 e 10  >>> [A] APROVADO! ')
print ('Entre 7.5 e 9.0 >>> [A] APROVADO! ')
print ('Entre 6.0 e 7.5 >>> [A] APROVADO! ')
print ('Entre 4.0 e 6.0 >>> [A] REPROVADO! ')
print ('Entre 4.0 e 0.0 >>> [A] REPROVADO!')
print ('='*40)

nota1 = float ( input ( 'Primeira nota ?  ' ))
nota2 = float ( input ( 'Segunda  nota ?  ' ))
m = (nota1 + nota2 ) / 2

if ( m <= 10 ) and ( m >= 9 ):
      print ( 'ALUNO OBTEVE NOTA >>> [A] APROVADO! ')
if ( m >= 7.5 ) and ( m < 9 ):
      print ('ALUNO OBTEVE NOTA >>> [B] APROVADO! ')
if ( m >= 6) and ( m < 7.5 ):
      print ('ALUNO OBTEVE NOTA >>> [C] APROVADO! ')
if ( m < 6 ) and ( m >= 4.5 ):
      print ('ALUNO OBTEVE NOTA >>> [D] REPROVADO! ')
if ( m >= 0 ) and ( m < 4.5 ):
      print ('ALUNO OBTEVE NOTA >>> [E]  REPROVADO! ')
