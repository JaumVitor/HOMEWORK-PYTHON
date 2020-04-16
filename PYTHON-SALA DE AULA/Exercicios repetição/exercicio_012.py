print(
    '§§§§§¹²¹²³ Partida de ping-pong ²¹²³³§§§§§'.upper())

jog1 = jog2 = diferença = 0
contador = 1
end = False
limite = 5

while not end:
    rodada = int ( input ('Quem marcou ponto na rodada [1/2] ?'))
    if rodada == 1:
        jog1 += 1
        contador += 1
    elif rodada == 2:
        jog2 += 1
        contador += 1
    else:
        print(
            'Jogada inválida, tente novamente')
    diferença = abs(jog1 - jog2)
    por = 2 - diferença

    print(
        f'Placar: {jog1} x {jog2} ')

    if (jog1 > 5) or (jog2 > 5):
        print (f'[Falta {por}]',end=' ') 

    if (( jog1 >= limite) or (jog2 >= limite)) and (diferença >= 2):
        break
if jog1 > jog2:
    ganhador = 'JOGADOR 1'
    print(f'O ganhador da partida de Ping-Pong foi {ganhador}, com resultado de {jog1} x {jog2}')
else:
    ganhador = 'JOGADOR 2'
    print (f'O ganhador da partida de Ping-Pong foi {ganhador}, com resultado de {jog2} x {jog1}')
    




