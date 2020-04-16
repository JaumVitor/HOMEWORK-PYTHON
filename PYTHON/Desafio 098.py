from time import sleep

def contagem(inicio, fim, passo):	#Função para contagem númerica
	print('~' * 43)
	print(f'Contagem númerica de {inicio} até {abs(fim)} pulando de {abs(passo)}')
	print ('> ',end='')
	for c in range(inicio, fim , passo):
		sleep(0.5)
		print(c, end=' ')
	sleep(1)
	print('FIM!')
	print('~' * 43)

def escreva(palavra):	#Função para alinhamento de frases 
	n = (len (palavra) + 4) // 2
	print ('-+' * n)
	print (f'  {palavra}')
	print ('-+' * n)

#progama principal 
contagem(1, 10, 1)
contagem(10, 0, -2)

escreva('Agora será sua vez de personalizar a contagem!')
i = int (input ('inicio: '))
f = int (input ('Fim:    '))
p = int (input ('Passo:  '))

if f < i:			#Caso o usuário queira uma contagem decrecente
	p = p * -1
	f = f - 1
else:
	f = f + 1

contagem(i, f , p)

