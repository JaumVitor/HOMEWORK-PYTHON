from random import randint

def escreva(palavra):	#Escreva algo sublinhando 
	t = len(palavra)
	print ('-=' * t)
	print (f'  {palavra}')
	print('-=' * t)

def maior(*numeros):  #Função maior()
	print ('-=' * 30)
	print ('Analizando os valores sortedos...')
	for i, c in enumerate(sorted(lista)):
		if i == 0:
			m = c
		else:
			if c > m:
				m = c
		print(c, end=' ')

	n = len(lista)
	print (f'Foram sorteador {n} valores\n')
	print (f'Dos valores destacados o número {m} é o maior!')
	print ('-=' * 30)

def max(*numeros):
	print('-=' * 30)
	print('Analizando os valores DESENVOLVIDOS...')
	cont = 0 
	for c in sorted(numeros):
		if cont == 0:
			m = c
		else:
			if c > m:
				m = c
		cont += 1
		print(c, end=' ')
	
	print(f'Foram cadastrados {len(numeros)} valores\n')
	print(f'Dos valores destacados o número {m} é o maior!')
	print('-=' * 30)


lista = list()
cont = 0
while cont < 7:
	valor = randint(1,15)
	if not valor in lista:
		cont += 1
		lista.append(valor)

maior(lista)	#$ Utilizando a função maior()

lista = list()
cont = 0 
while cont < 5:
	valor = randint(1, 10)
	if not valor in lista:
		cont += 1
		lista.append(valor)

maior(lista)

max(1,2,5,3,4,9)
max(7,8,6,9,4,14,11)
max(0)