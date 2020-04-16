# Parte da descrição do catalizador

print ('='*62)
print ('                              DESCRIÇÃO DO "CATALIZADOR"                                ')
print ('='*62)
print ('[1º] > Irá digitar o número de jogos! (Quantos serão observados nessa rodada) ')
print ('[2°] > Digitar os jogos com resultados oficiais (O verdadeiro placar dos jogos)')
print ('[3°] > Selecionara os jogadores titulares (Nome')
print ('[4º] > Relate quais serão seus palpites, para dar inicio a catalização  ')
print ('[5º] > O progama ira execultar quais de seus jogadores mais marcou gol !')
print ('='*62,'\n')

# Parte da digitação dos jogos oficiais ( os quais serão usados para a comparação )
# Parte complicada pois é necessário usar os palpites para 7 possibildades de jogos 

njogo = int ( input ('[1º] PRECISO QUE VOCÊ DIGITE O NÚMERO DE JOGOS QUE SERÃO ANÁLISADOS: '))
print (' ')
print ('='*62)
print ('='*62)

if ( njogo == 1 ) :
   print ('[2º] DIGITE OS RESULTADOS VERDADEIROS ( ABAIXO ) ')
   of1_1 = int ( input ('1º JOGO >>> Casa ? '))
   of1_2 = int ( input ('1º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of1_1, of1_2))
   print ('='*62)
   print ('='*62)
   
elif ( njogo == 2 ) :
   print ('[2º] DIGITE OS RESULTADOS VERDADEIROS ( ABAIXO ) ')
   of2_1 = int ( input ('1º JOGO >>> Casa ? '))
   of2_2 = int ( input ('1º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of2_1, of2_2))
   print ('- '*62)

   of2_3 = int ( input ('2º JOGO >>> Casa ? '))
   of2_4 = int ( input ('2º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of2_3, of2_3))
   print ('='*62)
   print ('='*62)

elif ( njogo == 3) :
   print ('[2º] DIGITE OS RESULTADOS VERDADEIROS ( ABAIXO ) ')
   of3_1 = int ( input ('1º JOGO >>> Casa ? '))
   of3_2 = int ( input ('1º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of3_1, of3_2))
   print ('- '*62)

   of3_3 = int ( input ('2º JOGO >>> Casa ? '))
   of3_4 = int ( input ('2º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of3_3, of3_4))
   print ('- '*62)

   of3_5 = int ( input ('3º JOGO >>> Casa ? '))
   of3_6 = int ( input ('3º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of3_5, of2_6))
   print ('='*62)
   print ('='*62)

elif ( njogo == 4) :
   print ('[2º] DIGITE OS RESULTADOS VERDADEIROS ( ABAIXO ) ')
   of4_1 = int ( input ('1º JOGO >>> Casa ? '))
   of4_2 = int ( input ('1º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of4_1, of4_2))
   print ('- '*62)

   of4_3 = int ( input ('2º JOGO >>> Casa ? '))
   of4_4 = int ( input ('2º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of4_3, of4_4))
   print ('- '*62)

   of4_5 = int ( input ('3º JOGO >>> Casa ? '))
   of4_6 = int ( input ('3º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of4_5, of4_6))
   print ('- '*62)

   of4_7 = int ( input ('4º JOGO >>> Casa ? '))
   of4_8 = int ( input ('4º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of4_7, of4_8))
   print ('='*62)
   print ('='*62)

elif ( njogo == 5) :
   print ('[2º] DIGITE OS RESULTADOS VERDADEIROS ( ABAIXO ) ')
   of5_1 = int ( input ('1º JOGO >>> Casa ? '))
   of5_2 = int ( input ('1º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of5_1, of5_2))
   print ('- '*62)

   of5_3 = int ( input ('2º JOGO >>> Casa ? '))
   of5_4 = int ( input ('2º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of5_3, of5_4))
   print ('- '*62)

   of5_5 = int ( input ('3º JOGO >>> Casa ? '))
   of5_6 = int ( input ('3º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of5_5, of5_6))
   print ('- '*62)

   of5_7 = int ( input ('4º JOGO >>> Casa ? '))
   of5_8 = int ( input ('4º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of5_7, of5_8))
   print ('- '*62)

   of5_9 = int ( input ('5º JOGO >>> Casa ? '))
   of5_10 = int ( input ('5º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of5_9, of5_10))
   print ('='*62)
   print ('='*62)

elif ( njogo == 6) :
   print ('[2º] DIGITE OS RESULTADOS VERDADEIROS ( ABAIXO ) ')
   of6_1 = int ( input ('1º JOGO >>> Casa ? '))
   of6_2 = int ( input ('1º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of6_1, of6_2))
   print ('- '*62)

   of6_3 = int ( input ('2º JOGO >>> Casa ? '))
   of6_4 = int ( input ('2º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of6_3, of6_4))
   print ('- '*62)

   of6_5 = int ( input ('3º JOGO >>> Casa ? '))
   of6_6 = int ( input ('3º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of6_5, of6_6))
   print ('- '*62)

   of6_7 = int ( input ('4º JOGO >>> Casa ? '))
   of6_8 = int ( input ('4º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of6_7, of6_8))
   print ('- '*62)

   of6_9 = int ( input ('5º JOGO >>> Casa ? '))
   of6_10 = int ( input ('5º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of6_9, of6_10))
   print ('- '*62)

   of6_11 = int ( input ('6º JOGO >>> Casa ? '))
   of6_12 = int ( input ('6º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of6_11, of6_12))
   print ('='*62)
   print ('='*62)

elif ( njogo == 7) :
   print ('[2º] DIGITE OS RESULTADOS VERDADEIROS ( ABAIXO ) ')
   of7_1 = int ( input ('1º JOGO >>> Casa ? '))
   of7_2 = int ( input ('1º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of7_1, of7_2))
   print ('- '*62)

   of7_3 = int ( input ('2º JOGO >>> Casa ? '))
   of7_4 = int ( input ('2º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of7_3, of7_4))
   print ('- '*62)

   of7_5 = int ( input ('3º JOGO >>> Casa ? '))
   of7_6 = int ( input ('3º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of7_5, of7_6))
   print ('- '*62)

   of7_7 = int ( input ('4º JOGO >>> Casa ? '))
   of7_8 = int ( input ('4º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of7_7, of7_8))
   print ('- '*62)

   of7_9 = int ( input ('5º JOGO >>> Casa ? '))
   of7_10 = int ( input ('5º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of7_9, of7_10))
   print ('- '*62)

   of7_11 = int ( input ('6º JOGO >>> Casa ? '))
   of7_12 = int ( input ('6º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of7_11, of7_12))
   print ('- '*62)

   of7_13 = int ( input ('7º JOGO >>> Casa ? '))
   of7_14 = int ( input ('7º JOGO >>> Fora ? '))
   print ('Resultado do primeiro jogo >>> {} x {}'.format(of7_13, of7_14))
   print ('='*62)
   print ('='*62)

elif ( njogo > 7 ):
   print ( ' ' )
   print ('SORRY, Ainda não podemos análizar mais de 7 resultados  :( ')
   print ('Por favor digite um número  abaixo de "7" para começar a catalizar ')

# Etapa para receber nome dos jogadores titulares

print ('[3] NESSA ETAPA URGE O NOME DOS 8 JOGODORES TITULARES ex:( HERO 11 )')

jog1 = str ( input ('NOME DO 1º TITULAR: '))
jog2 = str ( input ('NOME DO 2º TITULAR: '))
jog3 = str ( input ('NOME DO 3º TITULAR: '))
jog4 = str ( input ('NOME DO 4º TITULAR: '))
jog5 = str ( input ('NOME DO 5º TITULAR: '))
jog6 = str ( input ('NOME DO 6º TITULAR: '))
jog7 = str ( input ('NOME DO 7º TITULAR: '))
jog8 = str ( input ('NOME DO 8º TITULAR: '))

# Agora vem a parte mais complicada ainda , precisamos fazer tudo corretamento para conseguir o resultado correto
# Colocar todos os paltites e suas possibilidades quado ('njogos' for igual a 1)
# Temos que fazer isso para os 8 jogadores titulares 

if ( njogo == 1 ):
    print ('='*62)
    print ('='*62)
    print ('DIGITE OS PALPITES DO {}'.format(jog1))
    j1_1 = int ( input ('1º JOGO >>> CASA ? '))
    j1_2 = int ( input ('1º JOGO >>> FORA ?'))
    if ( njogo == 1 ) and ( j1_1 == of1_1 ) and ( j1_2 == of1_2 ):
      print ('Gooooll do {} >>> ESTE JOGADOR ACERTOU O PALPITE  {} x {}'.format(jog1, j1_1, j1_2 ))
    else :
      print ('{} não marcou gol nesse palpite :('.format(jog1))
    print ('* '*62)

    print ('DIGITE OS PALPITES DO {}'.format(jog2))
    j2_1 = int ( input ('1º JOGO >>> CASA ? '))
    j2_2 = int ( input ('1º JOGO >>> FORA ?'))
    if ( njogo == 1 ) and ( j2_1 == of1_1 ) and ( j2_2 == of1_2 ):
      print ('Gooooll do {} >>> ESTE JOGADOR ACERTOU O PALPITE  {} x {}'.format(jog2, j2_1, j2_2 ))
    else :
      print ('{} não marcou gol nesse palpite :('.format(jog2))
    print ('* '*62)
    
    print ('DIGITE OS PALPITES DO {}'.format(jog3))
    j3_1 = int ( input ('1º JOGO >>> CASA ? '))
    j3_2 = int ( input ('1º JOGO >>> FORA ?'))
    if ( njogo == 1 ) and ( j3_1 == of1_1 ) and ( j3_2 == of1_2 ):
      print ('Gooooll do {} >>> ESTE JOGADOR ACERTOU O PALPITE  {} x {}'.format(jog3, j3_1, j3_2 ))
    else :
      print ('{} não marcou gol nesse palpite :('.format(jog3))
    print ('* '*62)
    
    print ('DIGITE OS PALPITES DO {}'.format(jog4))
    j4_1 = int ( input ('1º JOGO >>> CASA ? '))
    j4_2 = int ( input ('1º JOGO >>> FORA ?'))
    if ( njogo == 1 ) and ( j4_1 == of1_1 ) and ( j4_2 == of1_2 ):
      print ('Gooooll do {} >>> ESTE JOGADOR ACERTOU O PALPITE  {} x {}'.format(jog4, j4_1, j4_2 ))
    else :
      print ('{} não marcou gol nesse palpite :('.format(jog4))
    print ('* '*62)
    
    print ('DIGITE OS PALPITES DO {}'.format(jog5))
    j5_1 = int ( input ('1º JOGO >>> CASA ? '))
    j5_2 = int ( input ('1º JOGO >>> FORA ?'))
    if ( njogo == 1 ) and ( j5_1 == of1_1 ) and ( j5_2 == of1_2 ):
      print ('Gooooll do {} >>> ESTE JOGADOR ACERTOU O PALPITE  {} x {}'.format(jog5, j5_1, j5_2 ))
    else :
      print ('{} não marcou gol nesse palpite :('.format(jog5))
    print ('* '*62)
    
    print ('DIGITE OS PALPITES DO {}'.format(jog6))
    j6_1 = int ( input ('1º JOGO >>> CASA ? '))
    j6_2 = int ( input ('1º JOGO >>> FORA ?'))
    if ( njogo == 1 ) and ( j6_1 == of1_1 ) and ( j6_2 == of1_2 ):
      print ('Gooooll do {} >>> ESTE JOGADOR ACERTOU O PALPITE  {} x {}'.format(jog6, j6_1, j6_2 ))
    else :
      print ('{} não marcou gol nesse palpite :('.format(jog6))
    print ('* '*62)
    
    print ('DIGITE OS PALPITES DO {}'.format(jog7))
    j7_1 = int ( input ('1º JOGO >>> CASA ? '))
    j7_2 = int ( input ('1º JOGO >>> FORA ?'))
    if ( njogo == 1 ) and ( j7_1 == of1_1 ) and ( j7_2 == of1_2 ):
      print ('Gooooll do {} >>> ESTE JOGADOR ACERTOU O PALPITE  {} x {}'.format(jog7, j7_1, j7_2 ))
    else :
      print ('{} não marcou gol nesse palpite :('.format(jog7))
    print ('* '*62)
    
    print ('DIGITE OS PALPITES DO {}'.format(jog8))
    j8_1 = int ( input ('1º JOGO >>> CASA ? '))
    j8_2 = int ( input ('1º JOGO >>> FORA ?'))
    if ( njogo == 1 ) and ( j8_1 == of1_1 ) and ( j8_2 == of1_2 ):
      print ('Gooooll do {} >>> ESTE JOGADOR ACERTOU O PALPITE  {} x {}'.format(jog8, j8_1, j8_2 ))
    else :
      print ('{} não marcou gol nesse palpite :('.format(jog8))
    print ('* '*62)

# Agora sera a segunda parte do processo, iremos coloccar os palpites ('quando njogo == 2')
# Esse progama está ficando gigante 

# UMAS OBSERVAÇÕES SÃO NECESSÁRIAS PARA NÃO SE PERDER 
	# 1- QUANDO ( njogos == 1 ) para o primeiro jogador será usado o ( of1_1 e of1_2 ), pois é apenas um jogo a ser analisado 
	# 2- PORÉM QUANDO ( njogos == 2 ) para o primero jogador E PRIMERO JOGO será usado o ( of2_1 e of2_2 ) <- para o primeiro jogo
	# 2- ADEMAIS QUANDO ( njogos == 2 ) para o primero jogador E SEGUNDO JOGO será usado o ( of2_3 e of2_4 ) <- para o segundo jogo
