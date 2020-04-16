from random import randint

maquina = randint(1, 10)

contador = 0
while True:
    jogador = ' '    
    while not jogador in 'IiPp':
        jogador = str(input('Qual sua jogada (P/I)? ')).strip()[0]

    número = int (input ('Informe o número da sua jogada: '))
    resultado = maquina + número
    print ('')

    if jogador in 'Pp':
        if resultado % 2 == 0:
            contador += 1 
            print (f'Parabéns, vc ganhou...a maquina digitou {maquina} e o resultado foi {resultado}')
        else:
            print ('Que pena, vc perdeu o game')
            break 

    elif jogador in 'Ii':
        if resultado % 2 != 0:
            contador += 1 
            print (f'Parabéns, vc ganhou... a maquina digitou {maquina} e o resultado foi {resultado}')
        else:
            print ('Que pena, vc perdeu...nesse caso é GAME OVER!')
            break
    print ('Vamos jogar novamente...')
    print ('-'* 50)
print(f'Conseguiu vencer {contador} vezes concecutiva')
