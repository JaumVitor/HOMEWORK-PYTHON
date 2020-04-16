from random import randint	# randint (Escolhe aleatóriamente números entre valores)
from time import sleep

lista = list()
def sorteia(valores):
	#Função de sortear e guardar dentro da lista
	lista.append(valores)

def somaPar(numeros):
	#Somar somente os números pares 
	soma = 0 
	for p in numeros:
		if p % 2 == 0:
			soma += p
	print(soma)

def digitar(palavra):
	for letra in palavra:
		print(letra, end='')
		sleep(0.05)
		
cont = 0 
while cont < 5:
	n = randint(0, 10) 
	if n not in lista: 
		sorteia(n)
		cont += 1

digitar('OS VALORES SORTEADOS SÃO: ')
for valores in lista:
	sleep(1)
	print(valores, end=', ')
print ('PRONTO')
sleep(1)

print(' >> E a soma dos valores PARES é', end=' ')
somaPar(lista)
