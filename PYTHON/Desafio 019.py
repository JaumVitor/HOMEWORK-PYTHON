import random
n1 = str ( input ('Participante 1 > '))
n2 = str ( input ('Participante 2 > '))
n3 = str ( input ('Participante 3 > '))
n4 = str ( input ('Participante 4 > '))

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print('O grande contemplado para apagar o quadro é {}'.format(escolhido))
