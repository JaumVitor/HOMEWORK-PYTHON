from random import shuffle

n1 = str ( input ('Participante 1 > '))
n2 = str ( input ('Participante 2 > '))
n3 = str ( input ('Participante 3 > '))
n4 = str ( input ('Participante 4 > '))

tudle = [n1, n2, n3, n4]
esc = shuffle (tudle)
print ('Nova ordem de classificação é {}'.format(tudle))
