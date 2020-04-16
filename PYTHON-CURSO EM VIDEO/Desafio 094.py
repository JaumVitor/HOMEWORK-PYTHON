dados = dict()      #Procriação de dados 
lista = list()

resultados = dict()  #Parte do resultado 
mulheres = list()
acima_média = list()

while True:
    dados['nome'] = str(input('* Nome: ')).capitalize().strip()
    while True:
        dados['genero'] = str(input('* Gênero (M/F) ? ')).upper()[0].strip()
        if dados['genero'] in 'MF':
            break
        else:
            print('    // Por favor, digite apenas M/F...tente novamente!  ')
            
    dados['idade'] = int(input('* Idade: '))
    lista.append(dados.copy())
    dados.clear()

    while True:
        next = str(input('    >> Ainda quer prosseguir com a análise (S/N) ? ')).upper()[0].strip()
        print ('-')
        
        if next in 'SN':
            break

    if next in 'N':
        break

resultados['pessoas'] = len(lista)  # A) Quantas pessoas cadastradas 

soma = 0               
for x in lista:
    if x['genero'] in 'F':
        mulheres.append(x['nome'])  #C) Adicionando num lista somente as mulheres (mulheres = list())
    #soma das idades
    soma += x['idade']  

resultados['media'] = soma / len(lista)     #B)  Média das idades (dict = {resultados['media']})

acima = list()

for x in lista:
    if x['idade'] > resultados['media']:    #D) Lista com as pessoas acima da média (acima_media)
        acima.append(x['nome'])
        acima.append(x['idade'])

        acima_média.append(acima[:])
        acima.clear()

print(f'A) Foram cadastradas {resultados["pessoas"]} pessoas')
print (f'B) A média das idades é {resultados["media"]:.1f} ')

print ('C) Mulheres analisadas',end=' >> ')
for i in mulheres:
    print(i, end=' ')
print ()

print('D) Lista das pessoas em acima da média', end=' ')
cont = 0
for i,c in enumerate (acima_média):
    for x in range (len(acima_média[i])):
        print(c[x], end=' ')

    cont += 1

    if len(acima_média) > cont:
        print (',',end='')
        

