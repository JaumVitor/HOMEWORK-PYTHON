print('-=' * 25)
print('VAMOS JOGAR JOkENPO ?!')
print('-=' * 25)

print('''instruções....
> Para começar a jogar escolha PEDRA, PAPEL ou TESOURA
> Logo depois o "Goku" irá escolher simuntaneamente 
> Boa sorte, e tente a sorte contra o Goku! ;) ''')
print ('==' * 25)

from time import sleep
from random import choice

jog = str(input('Informe sua jogada : ').upper())
print('- ' * 25)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print ('PO!')

print('**' * 25)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
npc = choice(lista)

if jog == 'PEDRA' and npc == 'PEDRA':        #condições para casos de empate 
    print('Hum...Tivemos um EMPATE! :/')
    print('Sua jogada foi {} e a minha também foi {}'.format(jog, npc))
    print('==' * 25)
elif jog == 'TESOURA' and npc == 'TESOURA':
    print('Hum...Tivemos um EMPATE! :/')
    print('Sua jogada foi {} e a minha também foi {}'.format(jog, npc))
    print('==' * 25)
elif jog == 'PAPEL' and npc == 'PAPEL':
    print('Hum...Tivemos um EMPATE! :/')
    print('Sua jogada foi {} e a minha também foi {}'.format(jog, npc))
    print('==' * 25)

elif jog == 'PEDRA' and npc == 'TESOURA':    #condições para casos de vitória 
    print('urrhh!!...Tenho que adimitir que VC GANHOU! >:(  ')
    print('Sua jogada foi {} e a minha foi {}'.format(jog, npc))
    print('==' * 25)
elif jog == 'PAPEL' and npc == 'PEDRA':
    print('urrhh!!...Tenho que adimitir que VC GANHOU! >:(  ')
    print('Sua jogada foi {} e a minha foi {}'.format(jog, npc))
    print('==' * 25)
elif jog == 'TESOURA' and npc == 'PAPEL':
    print('urrhh!!...Tenho que adimitir que VC GANHOU! >:(  ')
    print('Sua jogada foi {} e a minha foi {}'.format(jog, npc))
    print('==' * 25)

elif jog == 'PEDRA' and npc == 'PAPEL':      #condições para casos de derrota 
    print('HAHA! Não foi dessa vez jovem rapaz...VC PERDEU :O ')
    print ('Sua jogada foi {} e a minha foi {}'.format(jog , npc))
    print('==' * 25)
elif jog == 'PAPEL' and npc == 'TESOURA':
    print('HAHA! Não foi dessa vez jovem rapaz...VC PERDEU :O ')
    print ('Sua jogada foi {} e a minha foi {}'.format(jog , npc))
    print('==' * 25)
elif jog == 'TESOURA' and npc == 'PEDRA':
    print('HAHA! Não foi dessa vez jovem rapaz...VC PERDEU :O ')
    print ('Sua jogada foi {} e a minha foi {}'.format(jog , npc))
    print('==' * 25)

else:
    print ('# SUA JOGADA FOI CLASSIFICADA COMO INVÁLIDA! ')
