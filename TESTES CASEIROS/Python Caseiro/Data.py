data_atual = str ( input ('Data atual ? ')).strip().split('/')
data_nasc = str ( input ('Data de nascimento ? ')).strip().split('/')

# idade do indivíduo será cauculada por esse algoritimo

if ( int( data_atual[0]) < 31) and ( int(data_atual[1]) <= 12) and ( int(data_nasc[0]) < 31 ) and ( int(data_nasc[1]) <= 12 ):
    
    if int(data_nasc[1]) > int(data_atual[1]): 
        idade = ( int( data_atual[2]) - int( data_nasc[2])) - 1 
    elif int( data_nasc[1]) == int( data_atual[1]) and int( data_nasc[0]) > int( data_atual[0]):
        idade = ( int( data_atual[2]) - int( data_nasc[2])) - 1
    else :
        idade = int( data_atual[2]) - int( data_nasc[2])
        
# A quantidade de meses que o indivíduo terá sera cauculada por este algoritimo, para isso temos que saber a sua idade exata 

    if int( data_atual[1] ) < int( data_nasc[1]):
        mes = ( idade * 12 ) + ( 12 - ( int(data_nasc[1]) - int( data_atual[1])))
    elif int( data_atual[1]) >= int( data_nasc[1]): 
        mes = ( idade * 12 ) + ( int( data_atual[1]) - int( data_nasc[1]))
# Para saber a quantidade de dias que o indivíduo terá sera cauculada por este algoritimo, para isso temos que saber seus meses 

    dias = mes * 30
     
    if int(data_atual[0]) < int(data_nasc[0]):
        dias_total = dias + (int(data_nasc[0]) - int(data_atual[0]))
    elif int(data_nasc[0]) < int(data_atual[0]):
        dias_total = dias + ( int(data_atual[0]) - int(data_nasc[0]))    
else :
    print(
        'Data inválida, digite uma data correta !')
print(
    f'Sua idade de {idade} anos\nTem {mes} meses de vida\nE curtiu aproximadamente {dias_total} dias' )
