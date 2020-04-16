frase = '[ELEIÇÕES PRESIDÊNCIAIS]'
frase1 = '[VOTE COM MODERAÇÃO]'

print(f'''
{frase:°^50}
Serra = 45
Dilma = 13
Ciro Gomes = 23
Indeciso = 99
Outros = 98
Nulo/branco = 0

{frase1:°^50}
''')

votos_total = serra = dilma = ciro = indeciso = outros = nulo = 0
voto = 1

while voto != 999:
    voto = int ( input ('Informe o seu voto para pesquisa: '))

    if voto == 45:
        serra += 1
        print('DECISÃO CONFIRMADA! ')
        votos_total += 1
    elif voto == 13:
        dilma += 1
        print('DECISÃO CONFIRMADA! ')
        votos_total += 1
    elif voto == 23:
        ciro += 1
        print('DECISÃO CONFIRMADA! ')
        votos_total += 1
    elif voto == 99:
        indeciso += 1  
        print('DECISÃO CONFIRMADA! ')
        votos_total += 1
    elif voto == 98:
        outros += 1
        print('DECISÃO CONFIRMADA! ')
        votos_total += 1
    elif voto == 0:
        nulo += 1
        print('DECISÃO CONFIRMADA! ')
        votos_total += 1
    elif voto == 999:
        break
    else:
        print('Voto inválido, tente novamente...'.upper())
        while (voto != 45) and (voto != 13) and (voto != 23) and (voto != 99) and( voto != 98 ) and ( voto != 0):  
            if voto == 999:
                break
            voto = int(input('Qual seu voto ? '))
            
            if (voto == 45) or (voto == 13) or (voto == 23) or (voto == 99) or (voto == 98) or (voto == 0):
                print('DECISÃO CONFIRMADA! ')
                votos_total += 1

#--------------------------------------------------------------------------------------------------------------------------

serra_porcentagem = ( serra * 100 ) // votos_total  
dilma_porcentagem = ( dilma * 100 ) // votos_total   
ciro_porcentagem = ( ciro * 100 ) // votos_total   
indeciso_porcentagem = ( indeciso * 100 ) // votos_total   
outros_porcentagem = ( outros * 100 ) // votos_total   
nulo_porcentagem = ( nulo * 100 ) // votos_total  

votos_validos = dilma + ciro + serra

dilma_turno = ( dilma * 100 ) // votos_validos 
serra_turno = ( serra * 100 ) // votos_validos 
ciro_turno = ( ciro * 100 ) // votos_validos 

metade_votos_validos = votos_validos // 2

if dilma_turno < metade_votos_validos:                                  #obs não conseguimos descobrir se vai para
    resposta = 'Não haverá segundo turno... é unanime'                   #o segundo turno
elif serra_turno < metade_votos_validos:
    resposta = 'Não haverá segundo turno... é unanime'
elif ciro_turno < metade_votos_validos:
    resposta = 'Não haverá segundo turno... é unanime'
else:
    resposta = 'Haverá segundo turno...'
    
frase2 = 'APURAÇÃO DOS VOTOS'
print(f'''
{frase2:°^50}
Dilma:    {dilma_porcentagem}%
Serra:    {serra_porcentagem}%
Ciro:     {ciro_porcentagem}%
Indeciso: {indeciso_porcentagem}%
Outros:   {outros_porcentagem}%  
Nulo:     {nulo_porcentagem}%
VOTOS:    {votos_total}
  
{resposta}''')
print ('°'*50)

