valor = float ( input ('Qual o valor ? '))
porcentagem = int ( input ('Valor do juros [ao mês] '))
porcentagem /= 100

end = True
continuar = 'S'

while end:
    for i in range(1, 12):
        soma = valor * porcentagem
        valor += soma  
    print(valor)

    continuar  = str ( input ('Deseja continuar com mais 1 ano S/N ? ')).strip().upper()
    if continuar  in 'N':
        break

    elif not continuar  in 'NS':
            continuar  = str(input('Deseja continuar com mais 1 ano S/N ? ')).strip().upper()


        
