genero = ''
idade = idade_18 = homens = mulheres_20 = 0

while True:
    genero = ' '
    while not genero in 'MmFf':
        genero = str(input('Genero M/F: ')).strip()
        if genero in 'Mm':
            homens += 1                  # Homenes cadastrados

        if not genero in 'FfMm':        
            print(                   
                'Dados invalidos, digite novamente! [M/F]\n') 
    
    idade = int(input('Idade ? '))
    if idade >= 18:
        idade_18 += 1                    # Idade maior que 18 anos, idependente de genero
    if (genero in 'Ff') and (idade <= 20):
        mulheres_20 += 1                  # Mulheres com menos de 20 anos 
         
    c = ' '
    while not c in 'SsNn':  
        c = str ( input ('Ainda quer analisar ? ')).strip()
        print ('')

    if c in 'Nn':
        break

print(
    f'''
Foram cadastrados {homens} homens
Temos tambem {mulheres_20} mulheres com menos de 20 anos
Ademais, {idade_18} Tem idade acima de 18 ''')
    


    
