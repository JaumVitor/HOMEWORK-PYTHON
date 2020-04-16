#Jogadores de futebol exercicio 093/1 - Guanabara 

inf = dict()
gols = list()
soma = 0

inf['nome'] = str (input ('Nome: '))
n = int (input (f'Quantas partidas {inf["nome"].upper()} jogou ? '))

print ()
for c in range (1,n + 1):
    gols.append(int(input(f'Quantos gols na {c}º partida ? ')))
    inf['marcou'] = gols

print ()
for x in inf['marcou']:
    soma += x
inf['total'] = soma     #poderia ter usado o sum(gols)...assim ele somaria a lista de gols

print ('-'*30)
print(inf)
print ('-'*30)

for key, values in inf.items():
    print (f' >> {key}: {values}')

print('-' * 30)

for partida, i in enumerate(inf['marcou']):
    print(f' > O jogador {inf["nome"]}, marcou {i} gols na {partida + 1}º partida.')
print (f'Obtendo um valor total de {inf["total"]} gols ')