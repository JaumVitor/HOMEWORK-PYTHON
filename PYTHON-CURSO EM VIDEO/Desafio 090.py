aluno = dict()

aluno['nome'] = str (input ('Nome: '))
aluno['media'] = float (input (f'Média d(a) {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif 7 > aluno['media'] >= 5 :
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
print ('-=' *15)

for keys,values in aluno.items():
    print (f'{keys:<8}: {values:^10}'.title())