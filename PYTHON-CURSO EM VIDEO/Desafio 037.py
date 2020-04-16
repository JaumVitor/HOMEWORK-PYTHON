import time 
num = int(input('Informe um número : '))
time.sleep(2)

print ('-=' * 30)
print('''Para aplicar a conversão considere as opções abaixo.
1 -> BINÁRIO 
2 -> HEXADECIMAL 
3 -> OCTAL ''')
print('-=' * 30)

opção = int ( input ('Informe qual a opção desejada : '))
print ( 'aguarde...')
time.sleep(2)
print('- ' * 30)
if opção == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print ('O número {} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
elif opção == 3:
    print ('O núemro {} convertido para OCTAL é {}'.format (num , oct(num)[2:]))
else:
    print('Opção inválida, tente novamente :(')
print ('-=' * 30)
