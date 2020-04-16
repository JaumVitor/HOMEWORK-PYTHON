lista = [2,4,5,7,10]

canal = 999
soma_pessoas = canal1 = canal2 = canal4 = canal5 = canal7 = canal10 = 0

while canal != 0:
    canal = int(input('Qual o canal que mais assiste ? '))
    
    if canal == 0:                  #Pra saida do progama
        break

    while not canal in lista:
        print('Por favor, informe um canal existente na lista...')
        canal = int(input('Qual o canal que mais assiste ? '))

    pessoas = int(input('Quantas pessoas assitem ? '))
    print (' ')

    if canal == 2:                  #Parte que faz as votações 
        canal2 += pessoas

    elif canal == 4:
        canal4 += pessoas

    elif canal == 5:
        canal5 += pessoas

    elif canal == 7:
        canal7 += pessoas
    
    elif canal == 10:
        canal10 += pessoas
    
total_votos = canal2 + canal4 + canal5 + canal7 + canal10 

porcentagem2 = ( canal2 * 100 ) / total_votos
porcentagem4 = ( canal4 * 100 ) / total_votos 
porcentagem5 = ( canal5 * 100 ) / total_votos
porcentagem7 = (canal7 * 100) / total_votos
porcentagem10 = (canal10 * 100) / total_votos

print (
f'''AUDIÊNCIA DOS CANAIS 

Canal 2 -- {porcentagem2:.1f}%
Canal 4 -- {porcentagem4:.1f}%
Canal 5 -- {porcentagem5:.1f}%
Canal 7 -- {porcentagem7:.1f}%
Canal 10 - {porcentagem10:.1f}%

 ''')

