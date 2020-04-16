# lista = [[],[],[]]        #Questão da prova de EStruturas 
# soma = 0

# n = int (input ('Número: '))
# for i in range(n):
#     lista[0].append(int (input ('Lista A: ')))
#     lista[1].append(int (input ('Lista B: ')))

# for x in range(len(lista[0])):      #Poderia ser a lista[1] pois as duas tem o mesmo tamanho
#     lista[2].append(lista[0][x] + lista[1][x])
    
# print(lista)

# for x in lista[0]:
#     print (x[1])

#-------------------------------------------------------------------------------------------
# palavra = ['estou desol ado']     #1 Resolução 
# p = list()

# for i in range (len(palavra[0])):
#     p.append(palavra[0][i])

#     if ' ' in palavra[0][i]:
#         p.remove(' ')
#         p.insert(i,'-')

# print(p)
# print (palavra)

# #------------------------------------------------------------------------------------------
# palavra = ['estou desol ado']      #Aprimoramento da resolução / palavra = list('Frase') 
# palavra[0:] = palavra[0]             

# # Metodo de fatiamento da palavra dentro da lista, podendo assim, usar a palavra que estava 
# # só  que de maneira totalmente pecorrida! cada letra separada

# for x, i in enumerate(palavra):

#     if ' ' in i:
#         palavra.remove(' ')
#         palavra.insert(x, '-')

# print(palavra)
#-------------------------------------------------------------------------------------------

# lista = [['Pedro',22,1],['Ana',43,2],['Jose',32,3]]

# print(lista)

# for x in lista:
#     print(x[0:3])

#--------------------------------------------------------------------------------------------

# lista = [None] * 5

# for x,i in enumerate (lista):
#     if i == None:
#         lista[x] = x

# print(lista)

#---------------------------------------------------------------------------------------------

# palavra = list('estudar bem'.upper())
# print(''.join(palavra))

#---------------------------------------------------------------------------------------------

