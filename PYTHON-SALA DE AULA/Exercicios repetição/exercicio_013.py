print(
    '''°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
    LISTA DOS ACRECIMOS
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
R$ 0,00 R$ 2.999,99--------25 %
R$ 3.000,00 R$ 5.999,99--- 20 %
R$ 6.000,00 R$ 9.999,99--- 15 %
Acima de R$ 10.000,00----- 10 %
===============================\n''')

resposta = 'S'
soma_salario = 0
soma_reajuste = 0

while not resposta in 'Nn':
    salario = float(input('Informe o salário do do trabalhador: '))
        
    if salario < 3000:
        reajuste = salario * 1.25
        print (f'O reajuste salárial foi alteredo para {reajuste:.2f} R$')
    elif 3000 <= salario < 6000:
        reajuste = salario * 1.20
        print (f'O reajuste salárial foi alteredo para {reajuste:.2f} R$')
    elif 6000 <= salario < 10000:
        reajuste = salario * 1.15
        print (f'O reajuste salárial foi alteredo para {reajuste:.2f} R$')  
    elif 10000 <= salario:
        reajuste = salario * 1.10
        print (f'O reajuste salárial foi alteredo para {reajuste:.2f} R$')
#=====================================================================================   
    soma_reajuste += reajuste
    soma_salario += salario 

    print(
        '-'* 50)
        
    resposta = str(input('Quer continuar S/N ? ')).upper().strip()[0]
    
    if resposta in 'Nn':
        break
    
    while ( resposta != 'N') and ( resposta != 'S') :
        print(
            'Valor inadequado, tente novamente digite S/N ')
        resposta = str(input('Quer continuar S/N ? ')).upper().strip()[0]
print ('')
print(
    f'Todos os salários reajustados: {soma_reajuste:.2f} R$\nTodos os salários antes do reajuste: {soma_salario:.2f} R$')
print(
    f'O aumento obitido nos salários de todos os trabalhadores foi de {soma_reajuste - soma_salario:.2f} R$ ')  
