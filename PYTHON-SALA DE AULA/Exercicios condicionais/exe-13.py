valor = float ( input (' TRABALHADORES -> Valor recebido por hora de trabalho: '))
hora1 = float ( input (' TRABALHADOR 1 -> Digite horas trabalhadas: '))
hora2 = float ( input (' TRABALHADOR 2 -> Digite horas trabalhadas: '))

sal1 = ( valor * hora1 )
sal2 = ( valor * hora2 )

if ( sal1 > sal2 ):
      print ('Salario do trabalhador 1 é maior ')
else:
      print ('Salario do trabalhador 2 é maior ')
