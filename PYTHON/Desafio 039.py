from datetime import date
from time import sleep


print ('-=' * 30)
print('{:^60}'.format('ALISTAMETO MILITAR'))
print('-=' * 30)

genero = str ( input('Informe seu gênero : ')).upper().strip()
if genero == 'FEMININO':
    print ('Aguade...')
    print('- ' * 30)
    sleep(2)
    print('Para mulheres não é obrigatório o alistameto militar')
    print('==' * 30)
elif genero == 'MASCULINO':
    ano = int(input('Informe o ano de nascimento : '))
    print ('Aguarde...')
    sleep(2)
    print('- ' * 30)
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade < 18:
        resto = 18 - idade 
        if resto == 1:
            print('Ainda não chegou o ano do seu alistamento...falta {} ano '.format(resto)) #Só para fins de concordância
            print ('O ano do seu alistamento será em {}'.format(ano + 18))
            print('==' * 30)
        else:
            print('Ainda não chegou o ano do seu alistamento...faltam {} anos '.format(resto))
            print ('O ano do seu alistamento será em {}'.format(ano + 18))
            print('==' * 30)
    elif idade > 18:
        resto = idade - 18
        if resto == 1:
            print('Já se passou {} ano do seu alistamento...'.format(resto)) #Só para fins de concordância
            print ('O ano do seu alistamento foi em {}'.format(ano + 18))
            print('==' * 30)
        else :
            print('Já se passaram {} anos do seu alistamento...'.format(resto))
            print('O ano do seu alistameto foi em {}'.format(ano + 18))
            print('==' * 30)
    else:
        print('Está no ano do seu alistamento...se informe IMEDIATAMENTE !')
        print('==' * 30)
        
