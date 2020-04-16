lista = list()
parentese_direita = list()
parentese_esquerda = list()

# lista.append(input('Informe a expressão: '))          #Minha resolução 

# for x in range(len(lista)):
#     for c in range(len(lista[x])):
#         if lista[x][c] in '(':
#             parentese_direita.append('(')
#         elif lista[x][c] in ')':
#             parentese_esquerda.append(')')

# if len(parentese_direita) == len(parentese_esquerda):
#     print ('Expressão válida!')      
# else:
#     print ('Expressão inválida')

expre = str (input('Informe a expressão: '))            #Resolução com ajuda do guanabara
                                                        #Poderia melhorar usando o expre.cont('(') 
for c in expre:                                            #sendo que esse valor deve ser igual a o outro para que a expressão seja válida
    if c in '(':
        parentese_direita.append('(')
    elif c in ')':
        parentese_esquerda.append(')')

if len(parentese_direita) == len(parentese_esquerda):
    print ('Expressão válida!')
else:
    print ('Expressão inválida')
