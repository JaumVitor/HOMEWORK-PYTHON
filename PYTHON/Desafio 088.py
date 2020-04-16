from random import randint
from time import sleep

sorteio = list()
numeros = list()

n = int (input ('Quantos jogos quer sortear ? '))

for jogos in range(n):
    for games_individuais in range(6):
        valor = randint(1, 60)

        if valor not in numeros:
            numeros.append(valor)
        else:
            while True:
                valor = randint(1,60)
                if valor not in numeros:
                    numeros.append(valor)
                    break

    sorteio.append(numeros[:])
    numeros.clear()

for posição in sorteio:
    posição.sort()
print ()

print ('PROCESSANDO',end=' ')
sleep(1)
print('.',end=' ')
sleep(1)
print('.',end=' ')
sleep(1)
print('.\n',end='')

print ('{:^20}'.format('JOGO DA MEGA-VIRADA!'))
for game in range (len(sorteio)):
    sleep(2)
    print(f'Jogo {game + 1}: ', end='')
    for indices in range(6):
        print(f'[ {sorteio[game][indices]:^2} ]',end=' ')
    print ()
