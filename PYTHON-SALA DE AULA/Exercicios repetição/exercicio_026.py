list = ['OTIMO', 'BOM', 'REGULAR', 'PESSIMO']

end = True
contador = 1

bom = otimo = regular = pessimo = soma = total = 0 

while end:
    idade = int(input(f'[{contador}] - Qual a sua idade ? '))
    contador += 1                       #Serve para ajudar a calcular a média 

    if idade == 0:
        break
    print ('')

    print('Otimo, Bom, Regular ou Pessimo ? ')
    opinião = str(input('O que achou do filme ? ')).strip().upper()
    print('-' * 50)

    if opinião in 'OTIMO':              #Votação 
        otimo += 1
        soma += idade
        total += 1 
        
    if opinião in 'BOM': 
        bom += 1
        total += 1 

    if opinião in 'REGULAR':
        regular += 1 
        total += 1 

    if opinião in 'PESSIMO':
        pessimo += 1
        total += 1 

    else:
        while not opinião in list:
            print('INFORME SUJESTÃO QUE ESTÃO LISTADAS!')
            print ('-')
            opinião = str ( input ('O que achou do filme ? ')).strip().upper()
            if opinião in list:
                print('-' * 50)
if otimo == 0:
    media = 0
else:
    media = soma / otimo
if bom == 0:
    porcentagem_bom = 0
else:
    porcentagem_bom = (bom * 100) / total

print(
f'''
ANÁLISE DE DADOS

Média das pessoas que responderam otímo: {otimo}
Pessoas que responderam regular: {regular}
Porcentagem dos quais escolheu BOM: {porcentagem_bom:.1f}%''')


    
