primeiro = int ( input ('Informe o primeiro termo da PG: '))
razão = int ( input ('Qual a razão ? '))
termos = int ( input ('Quantos termos ? '))

contador = 0
x = primeiro
while contador < termos:
    print (x)
    x += razão 
    contador += 1
