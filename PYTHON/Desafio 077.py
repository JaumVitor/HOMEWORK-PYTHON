palavras = 'aprender', 'progamar','praticar','estudar','habilidade','recortar','escola','python','televisão','guanabara'

vogais = ' '                #Maneira mais elaborada e mais bonitaa! 
cont = 0 
for i in range(len(palavras)):
    print(f'{palavras[i].capitalize():.<10} TEM ',end='')
    for x in range(len(palavras[i])):
        if palavras[i][x] in 'AaEeIiOoUu':
            vogais += palavras[i][x]
            cont += 1

    print(f'{cont} VOGAIS =>', end ='')
    print (vogais, end='')
    cont = 0
    vogais = ' '
    print ('')

# for p in palavras:              #Maneira mais simplificada 
#     print (f'{p.upper()} Vogais: ',end='')
#     for letra in p:
#         if letra.lower() in 'aeiou':
#             print(letra, end='')
#     print('')