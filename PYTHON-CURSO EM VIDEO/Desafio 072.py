extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

c = 'S'
while True:
    while True:
        n = int(input('Qual o número ? '))
        print ('-')

        if 0 <= n <= 20:
            break
        print ('Por favor digite um valor entre 0 e 20!')
    print(f'O número {n} escrito por extenso é "{extenso[n]}"'.upper())
    print('='*45)

    while True: 
        c = str(input('Quer continuar ? ')).upper()
        if c in 'SN':
            break
    if c in 'N':
        break
print ('Agradecemos a sua presença, volte sempre! ')

