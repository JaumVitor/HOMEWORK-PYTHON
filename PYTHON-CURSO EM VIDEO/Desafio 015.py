dia = int ( input ( 'Quantos dias passou com o carro ? '))
km = float ( input ( 'Quantos km foram rodados ? '))

custo = (dia * 60) + (km * 0.15)
print ( 'Valor do aluguel é de R${}'.format(custo ))
