# lista = list()

# lista.append('Guanabara')
# lista.append(43)

# galera = list()
# galera.append(lista[:])
# lista[0] = 'Hero'
# lista[1] = 19
# galera.append(lista[:])
# lista[0] = 'Jose'
# lista[1] = 2
# galera.append(lista[:])
# print (galera)

# lista = [['João Vitor', 18], ['Juliana', 34], ['Habreu', 43]]

# for gente in lista:
#     for c in range (len (gente[0])):
#        print(gente[0][c])

galera = list()
aluno = list()

for c in range(3):
    aluno.append(str (input ('Nome: ')))
    aluno.append(int (input ('Idade: ')))
    galera.append(aluno[:])
    aluno.clear()
print (galera)