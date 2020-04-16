print ('-' *50)
ano1  = int ( input ('Ano de nascimento ? '))
mes1 = int ( input ('Digite mês de nascimento: '))
dia1 = int ( input ('Dia que você nasceu: '))
ano2 = int ( input ('Ano atual: '))	
mes2 = int ( input ('Mês atual: '))
dia2 = int ( input ('Dia atual: '))
print ('-'*50)

idade1 = (ano2 - ano1) #variaveis 
idade2 = (idade1 - 1) #variaveis

if (mes2 >= mes1):
      print ('VOCÊ NASCEU NO DIA {}/{}/{}'.format(dia1, mes1,ano1))
      print ('VOCÊ ESTA NO DIA {}/{}/{}'.format(dia2, mes2, ano2))
      print ('')
      print ('Na data atual você se encotra com  {} anos de idade'.format(idade1))
else:
      print ('VOCÊ NASCEU NO DIA {}/{}/{}'.format(dia1, mes1, ano1))
      print ('VOCÊ NASCEU NO DIA {}/{}/{}'.format(dia2, mes2, ano2))
      print ('No ano atual você ainda se encontra com {} anos de idade'.format(idade2))
