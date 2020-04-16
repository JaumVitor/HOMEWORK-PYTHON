from random import randint
from time import sleep

frase = '[ vamos brincar.... escolha um número que esteja entre entre 0 e 10 e tente sua sorte! ]'.upper()
print(
    f'''{frase:°^123}
    ''')

pc = randint(0, 10)
end = True
tentativa = 0

while end:
    n = int(input('Digite o valor, e veja se acerta meu número: '))
    print('AGURDE...\n')
    tentativa += 1 
    sleep(2)

    if n == pc:
        break
    if n < pc:
        print('ERROU HAHA !, O meu número é maior!')
    elif n > pc:
        print ('ERROU HAHA !, Pense em um valor menor!')

print(f'PARÁBENS mizeravel ! vc acertou meu número com {tentativa} tentativas...ele era o {pc} > urrh! ')