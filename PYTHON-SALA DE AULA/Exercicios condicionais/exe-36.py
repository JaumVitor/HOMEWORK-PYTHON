nome = str ( input ('Digite seu nome : '))
turno = str ( input ('Qual seu turno ? '))

if ( turno == 'm') or ( turno == 'M'):
   print ('Bom dia, {}'.format( nome ))
elif ( turno == 't') or ( turno == 'T'):
   print ('Boa tarde, {}'.format ( nome ))
elif ( turno == 'n') or ( turno == 'T'):
   print ('Boa noite, {}'.format ( nome ))
