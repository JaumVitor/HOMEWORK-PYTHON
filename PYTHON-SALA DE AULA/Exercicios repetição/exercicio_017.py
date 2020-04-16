from time import sleep

cartão = True
peso_maior = peso_menor = altura_maior = altura_menor = 0
candidata_altura_maior = candidata_altura_menor = candidata_peso_maior = candidata_peso_menor = 0

frase1 = '[ CONCURSO DE BELEZA ]'
print ('_'*50)
print(f'''{frase1:^50}''')
print ('¨'* 50)

while cartão: 
    cartão = str(input('Quantos catões serão analisados ? '.upper())).upper().strip()
    print ('')
    if cartão == 'FIM':
        break
    for i in range (1, int(cartão) + 1):
        candidata = str(input(f'Informe o nome da {i}º candidata: '))
        altura = float ( input ('Qual o altura da garota ? '))
        peso = float(input('Qual o peso da garota ? '))
        print ('')

        if i == 1:
            peso_maior = peso 
            peso_menor = peso
            
            altura_maior = altura
            altura_menor = altura

            candidata_altura_maior = candidata
            candidata_altura_menor = candidata

            candidata_peso_maior = candidata
            candidata_peso_menor = candidata

#===========================================================================================
        if altura > altura_maior:          #Para fazer a analise de quem é o maior ou menor 
            altura_maior = altura
            candidata_altura_maior = candidata
            
        if altura < altura_menor:
            altura_menor = altura
            candidata_altura_menor = candidata

        if peso > peso_maior:
            peso_maior = peso 
            candidata_peso_maior = candidata 

        if peso < peso_menor:
            peso_menor = peso
            candidata_peso_menor = candidata
#============================================================================================           
sleep(1.5)
print('CARREGANDO DADOS, AGUARDE ALGUNS INSTÂNTES...')          #ENCERRAMENTO
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(2)

frase = '[ ANALISE DE DADOS ]'
print('_' * 50)                                                  
print(
    f'''{frase:°^50}

CANDIDATA MAIOR: {candidata_altura_maior} e mede {altura_maior}
CANDIDATA MENOR: {candidata_altura_menor} e mede {altura_menor}

PESO MAIOR: {candidata_peso_maior} e tem peso de {peso_maior}Kg
PESO MEOR: {candidata_peso_menor} e tem peso de {peso_menor}Kg 

''')
print('°'*50)       




    
