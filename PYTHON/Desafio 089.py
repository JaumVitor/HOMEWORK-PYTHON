alunos = list()             #listas dentro de listas -------------------------------
individuo = list()

while True:
    individuo.append(str(input('Nome  : ')).capitalize())
    individuo.append(float(input('Nota 1: ')))
    individuo.append(float(input('Nota 2: ')))

    alunos.append(individuo[:])
    individuo.clear()
    print ('<*>',end=' ')

    while True:
        back = str (input ('Next... Yes or No ? ')).strip().upper()[0]
        if back in 'NY':
            print ('-')
            break

    if back in 'N':
        break

for i,x in enumerate (alunos):
    media = ( x[1] + x[2]  ) / 2            #calculo da média aritimétrica dos alunos
    alunos[i].append(media)

print ('=-' * 15)
print ('{:^30}'.format('MÉDIA DOS ALUNOS'))
print('=-' * 15)
    
for c,x in enumerate (alunos):
    print(f'{c + 1}) {x[0]:.<23}{x[3]}')
print('=-' * 15)
print ()

while True:                    #Campo de validação de verificação -------------------
    valor = int(input('Quer verificar a nota de qual aluno ? '))
    
    if valor == 999:
        break
    
    if valor > len(alunos):
        while True:
            print ('<*> Aluno não encontrado na lista! <*>')
            valor = int(input('Qual o aluno será feita a analise ? '))

            if valor == 999:
                break

            if not valor > len(alunos):
                break

        if valor == 999:
            break

    print(f'ALUNO: {alunos[valor - 1][0]}.... NOTA: 1ª[{alunos[valor - 1][1]}] 2ª[{alunos[valor - 1][2]}]\n')

print ()
print ('{:°^45}'.format('OBRIGADO, VOLTE SEMPRE! '))
    
