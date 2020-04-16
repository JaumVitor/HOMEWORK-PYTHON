# valor = str(input('Infome o valor: ')).strip() # para saber quantos digitos

# tamanho = len(valor)
# print (tamanho)

valor = int(input('Digite o valor: '))   
cont = 0

while valor % 10 != 0 :
    valor = valor // 10
    cont += 1 
print (cont)