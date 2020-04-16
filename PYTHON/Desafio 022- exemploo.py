nome = str ( input ('Digite o seu nome completo: '))
print ('Seu nome em letras maisculas fica assim: ', nome.upper())
print ('seus nome em letras minsuculas fica assim: ', nome.lower())
print ('Quantidade de letras do seu nome: ', len ( nome.replace(' ','')))
nome = nome.split(' ')
print ('{}'.format (len(nome[0])))

print ('''codigo menor pra calcular o tamanho do nome inteiro:
nome = str(input('seu nome:')).strip()
print('seu nome tem {} letras'.format(len(''.join(nome.split()))))''')
