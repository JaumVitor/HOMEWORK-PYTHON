conteiner = int(input('Digite o número de conteiners: '.upper()))
print(
    '-' * 50)

soma_conteiner = 0

for i in range(1, conteiner + 1):
    peso_conteiner = float(input(f'Informe o peso do {i}º conteiners: '))
    soma_conteiner += peso_conteiner
print(
    f'O peso de todos os conteiners é {soma_conteiner}Kg\n')
    
passageiro = 1
soma_bagagem = 0
quantidade = 0

while passageiro != 0:
    print(
        '_' * 50)
    print(
        'Para encerrar a bilheteria digite [0]'.upper())
    print(
        '='* 50)
    passageiro = int(input('Qual o número do bilhete do passageiro ? '))
    if passageiro != 0:
        bagagem = float(input(f'Infome a quantidade de bagagem [CODIGO PASS.{passageiro}]: '))
        soma_bagagem += bagagem
        quantidade += 1 
        print(
            '')
    else:
        break
print(
    '')
#---------------------------------------------------------
peso_passageiro = quantidade * 70       #individual 
peso_bagagem = soma_bagagem * 10
#----------------------------------------------------------
peso_total_passageiro = peso_bagagem + peso_passageiro  #Bagagens + peso dos passageiros
#----------------------------------------------------------
peso_carga = soma_conteiner
#----------------------------------------------------------
peso_maximo = peso_carga + peso_total_passageiro   #PARA SABER SE O AERONAVE ESTA APTA PARA DECOLAR
#----------------------------------------------------------
limite = 500000                           #Peso da aeronave sem nenhuma adição 
combustivel = (limite - peso_maximo) / 1.5

x = '[AGÊNCIA DA AERONAUTICA]'   # titulo da descrição 
print(f'{x}\n')

if combustivel < 10000:
    print(
        f'''Acessibilidade de combustivel: está indequada para viagem, pois o saldo esta negativo > {combustivel:.2f}
Infelizmente não será possivel realizar a decolagem! ''')
else:
    print(
        f'''Acecibilidade de combustivel esta adequada para viagem > {combustivel:.2f}
Decolagem autorizada...Tenha uma boa viagem!''')

