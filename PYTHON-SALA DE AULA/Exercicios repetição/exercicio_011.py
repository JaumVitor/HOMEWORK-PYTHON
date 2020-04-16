print('========-----Calculo das médias-----=========\n'.upper())

matricula = 1
aluno = reprovado = aprovado = 0

while matricula != 0:
    matricula = int(input('Informe a sua matricula: '.upper()))
    print ('¹²³'* 15)
    if matricula != 0:
        aluno += 1 
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        nota3 = float(input('Digite a terceira nota: '))

        media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

        if media >= 7:
            aprovado += 1
        else:
            reprovado += 1
            
        print (f'O ALUNO DE nº [MATRICULA {matricula}] OBTEVE MEDIA {media}\n')
print(
    f'Dos {aluno} alunos que foram analizados:\nAPROVADOS: {aprovado}\nREPROVADO: {reprovado} ')     
