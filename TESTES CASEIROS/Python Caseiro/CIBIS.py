from time import sleep
from operator import itemgetter

oficial = str(input('Palpite oficial: ')).strip().split("/")
jogadores = int(input('Quantos jogadores vão participar na rodada ? '))
print ('-'* 50)
print ('Analizando',end=' ')
sleep(1)
print ('.',end=' ')
sleep(1)
print ('.',end=' ')
sleep(2)
print('.', end=' // OBS: Cada jogador deverá fazer ')
print (f'{len(oficial)} palpites //\n')

jogos = list()
palpites = list()
gols = 0

for jog in range(jogadores):        #Registrando palpites 
    jogos.append(input ('Nome: '))
    lista = list(str(input(f'Palpite Jogador {jog + 1}: ')).split("/"))
    
    if len(lista) == len(oficial):  #validação palpite, tem que ser do mesmo tamanho do oficial 
      jogos.append(lista)
    else:
      while True:
        print('<*> SEU PALPITE NÃO CONTEM O TAMANHO ADEQUADO! <*>')
        print ('-')
        lista = list(str(input('Palpite novamente: ')).split("/"))
        
        if len(lista) == len(oficial):    #Só adiciona na lista caso o tamnhao for o mesmo 
          jogos.append(lista)             #Para evitar erros no momento de analizar o gol
          break

    print ()
    print (f'<*> [PALPITE FEITO! BOA SORTE {jogos[0]}] <*>'.upper())
    print('-' * 50)

    palpites.append(jogos[:])
    jogos.clear()

#Primeira etapa concluida...(Armazenamento dentro das matrizes) [[nome,[palpites]],[nome,[palpites]],....]
#Agora será feito o calculos de gols

for n,c in enumerate (palpites):
  for x in range (len(c[1])):
    if c[1][x] == oficial[x]:   # pecorrendo toda lista de palpites e verificando se ela é igual a oficial
      gols += 1                 # Quando ela é igual o jogador marca gol 
  palpites[n].append(gols)
  gols = 0 

# Agora a lista se encontra dessa forma [[nome, [palpites],gols], [nome, [palpites],gols], ....]

jog = list()
rank = list()

for ranking in palpites:
  jog.append(ranking[0])
  jog.append(ranking[2])

  rank.append(jog[:])
  jog.clear()

rank.sort(key=itemgetter(1), reverse=True)  #Método de organização considerando apenas um elemento da lista

print('Carregando Classificação', end=' ')
sleep(1)
print('.', end=' ')
sleep(1)
print('.', end=' ')
sleep(2)
print('.', end='')

print('\n','_' * 33)
print('RANKING DOS JOGADORES DA RODADA')

print ('_'* 33)
print('{:<2} | {:<20} | {:<5}'.format('Nº', 'PARTICIPANTES', 'GOLS'))
print ('¨'*33)
for i,x in enumerate (rank):
  print (f'{i + 1}° | {x[0]:<20} | {x[1]:^5}'.capitalize())

print('=-=' * 11)
