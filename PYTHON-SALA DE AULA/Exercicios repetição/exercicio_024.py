primeiro = int(input('Informe o primeiro termo da PA: '))
razão = int(input('Qual a razão ? '))
termos = int(input('Quantos termos tem a PA ? '))
print('')

contador = 0
x = primeiro
while contador < termos:
    print(x, end=' , ')
    x *= razão
    contador += 1
print('FIM')
