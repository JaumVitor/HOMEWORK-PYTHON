from time import sleep

num = list()
pos_menor = list()
pos_maior = list()

for x in range(5):
    num.append(int(input(f'{x + 1}º Informe o número: ')))

menor = min(num)
maior = max(num)

cont_menor = cont_maior = 0 
for i in range(len(num)):           #for i,x in enumerate (num):
    if num[i] == menor :                 #if x == menor: 
        pos_menor.append(i)
    if num[i] == maior :               #Adicionei os valores na lista para dps usar eles
        pos_maior.append(i)            #Mas poderia ter feito direto nesse for 

print('')
print('CARREGANDO PROCESSAMENTO', end=' ')
sleep(1)
print ('.',end=' ')
sleep(1)
print ('.',end=' ')
sleep(1.5)
print('.\n')

print(f'O maior valor da lista é {maior}, se encontra na ',end=' ') 
for pos1 in pos_maior:
    print(f'{pos1 + 1}º',end='...')

print('') #quando for finalisada a sequncia de núemeros 

print(f'E o menor valor da lisa é {menor}, se encontra na ', end=' ')
for pos2 in pos_menor:
    print(f'{pos2 + 1}º', end='...')
    
print(' ola mundo')


