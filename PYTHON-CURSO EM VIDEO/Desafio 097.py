def escreva(palavra): #função para alinhamento de palavras
	tamanho = len(palavra) + 4
	print('~' * tamanho)
	print(f'  {palavra}')
	print ('~' * tamanho)

#progama principal 
escreva('texto'.upper())
escreva('americano'.upper())
escreva('PROJETO CURSO EM VIDEO')
escreva('ranking cibes cup internetional :)'.upper())
