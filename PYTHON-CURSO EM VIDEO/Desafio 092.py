from datetime import datetime

dados = dict()

dados['nome'] = str ( input ('> Nome: '))
dados['nascimento'] = int ( input ('> Nascimento: '))
dados['ctps Nº'] = int ( input ('> Cateira de trabalho Nº '))

dados['idade'] = datetime.now().year - dados['nascimento']

print ()
if dados['ctps Nº'] == 0:
    dados['ctps Nº'] = 'Não contém'
    for key,values in dados.items():
        print (f'   * {key}: {values}')

else:
    dados['contratação'] = int (input ('>> Ano de contratação: '))
    dados['salário'] = float ( input ('>> Salário R$'))
    dados['aposentadoria'] = (dados['contratação'] - dados['nascimento']) + 35
    
    print ()
    for key, values in dados.items():
        print (f'   * {key}: {values}')
