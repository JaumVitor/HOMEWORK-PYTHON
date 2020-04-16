print ('=' *40)
print ('QUAL É A DATA MAIS RECENTE')
print ('=' *40)
print ('PRIMEIRA DATA')
print ('o' *40)

dia1 = int ( input ('Dia ? ')) 
mes1 = int ( input ('Mês ? ')) 
ano1 = int ( input ('Ano ? ')) 
print ('-'*13, 'Primeira data','-'*13) 
print ('>>> {}/{}/{}'.format(dia1, mes1, ano1)) 

print ('-' *40)
print ('SEGUNDA DATA')
print ('o' *40)
	
dia2 = int ( input ('Dia ? ')) 
mes2 = int ( input ('mes ? ')) 
ano2= int ( input ('ano ? ')) 

print ('-'*13, 'Segunda data','-'*13) 
print ('>>> {}/{}/{}'.format(dia2, mes2, ano2)) 
print ('-' *40)

if (ano1 > ano2 ):
    print ('Primeira data é mais recente'.format (dia1, mes1, ano1, dia2, mes2, ano2)) 
elif (ano2 > ano1):
    print ('Segunda data é mais recente '.format (dia2, mes2, ano2, dia1, mes1, ano1)) 
    
elif (ano1 == ano2) and (mes1 > mes2):
    print ('Primeira data é mais recente') 
elif (ano2 == ano1) and (mes2 > mes1):
    print ('Segunda data é mais recente') 
    
elif (ano2 == ano1) and (mes2 == mes1) and (dia1> dia2):    
    print ('Primeira data é mais recente') 
elif (ano2 == ano1) and (mes2 == mes1) and (dia2 > dia1):
    print ('segunda data é mais recente') 
    
elif (ano1 == ano2) and (mes1 == mes2) and (dia1 == dia2) :
    print ('As datas são iguais') 

	
