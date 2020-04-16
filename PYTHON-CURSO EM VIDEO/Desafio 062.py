primeiro = int ( input ('Informe o primeiro: '))
razão = int ( input ('Qual a razão ? '))

contador = 1
n = primeiro
final = 0
x = 10

while x != 0:
    final = final + x
    while contador <=final :
        print (n, end=' , ')
        n = n + razão
        contador = contador + 1
    print('PAUSE')
    x = int(input('Quantos termos ainda quer ? '))
print (f'Progressão finalizada com {final} termos mostrados ')

# a1 = int(input('Primeriro termo: '))          RESOÇUÇÃO DOS INSCRITOS 
# r = int(input('A razão da PA: '))
# cont = 10
# termos = 0
# while not cont == 0:
#     print(a1, end=' → ')
#     cont += -1
#     termos += 1
#     a1 += r
#     if cont == 0:
#       cont = int(input('Acabou!\nMais quanto termos você quer ver?:'))
# print('FIM\n Progresso finalizado com {} termos'.format(termos))

        

