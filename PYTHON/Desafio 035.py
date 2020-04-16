print('-=' * 20)
print (' Alanisador de triangulo')
print('-=' * 20)
l1 = float ( input ('Digite o lado 1 do triangulo : '.upper()))
l2 = float ( input ('Informe o lado 2 do triangulo : '.upper()))
l3 = float ( input ('Informe o lado 3 do tringulo : '.upper()))

print ('-='*20)
if l1 + l2 > l3 and l3 + l2 > l1 and l3 + l1 > l2:
    print('Com esses valores é impossivel formar triangulo')
else:
    print ('Pode formar triangulo')
print('-='*20)
