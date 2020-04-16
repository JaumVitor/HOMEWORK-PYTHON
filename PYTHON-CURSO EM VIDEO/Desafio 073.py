tabela = ('São Paulo', 'Flamengo', 'Internacional', 'Grêmio', 'Palmeiras', 'Cruzeiro', 'Atlético-MG', 'Athletico-PR',
          'Santos', 'Botafogo', 'Bahia', 'Fluminense', 'Corinthians', 'Ceará', 'Vasco', 'Chapecoense','América-MG', 'Vitória', 'Paraná', 'Sport')

print ('{:=^50}'.format('[ TABELA BRASILEIÃO 2019 ]'))
for rank, i in enumerate (tabela):
    print(rank + 1, i)
print ('')

print('{:=^50}'.format('[ 5 PRIMEIROS DA TABELA ]'))
for i in range(0,5):         #Poderia usar tmb, a formatação | print(f'{tabela[0:5]}')
    print(i + 1, tabela[i])
print ('')

print('{:=^50}'.format('[ 4 ULTIMOS DA TABELA ]'))
ultimos = tabela[-4:]
for t in ultimos:
    print (':( ',t)

org = sorted(tabela)
print('{:=^50}'.format('[ TABELA NA ORDEM ALFABETICA ]'))
for pos, x in enumerate (org):
    print (f'{pos + 1 }° {x}')

posição = tabela.index('Chapecoense')
print('{:=^50}'.format('[ #FORÇA CHAPE ]'))
print(f'{tabela[posição]} está na {posição + 1}° posição\n')

