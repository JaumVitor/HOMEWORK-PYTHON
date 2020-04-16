def fatorial(valor, show=False):
	"""
	-> Calcula o fatorial de um numero
	
	param n = Numero oferecido para calcular o fatotial 
	param valor = Parametro que terá o valor da variavel "valor"
	param show = Caso esteja True, irá mostrar na tela o calculo fatórial, se não, mostra apenas o resultado 
	"""
	c = valor
	if show:
		print (valor,end='')
	while c > 1:
		c -= 1
		if show:
			print (f' x {c}',end ='')
		valor *= c
	if show:
		return (f' = {valor}')
	else:
		return f'O fatorial de {n} = {valor}'

n = int (input ('Quer calcular o fatórial de que número ? '))
print (fatorial(n,show=True))