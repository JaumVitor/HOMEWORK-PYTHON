from random import randint 
from operator import itemgetter

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}

rank = sorted(jogadores.items(),key=itemgetter(1),reverse= True)

print (rank)