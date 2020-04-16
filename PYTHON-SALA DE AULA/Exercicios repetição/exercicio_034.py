primeiro = int ( input ('Qual o primeiro termo ? '))
limite = int ( input ('Qual limite ? '))
razão = int ( input ('Qual a razão ? '))

for i in range(primeiro, limite, razão ):
    print(i)
print ('FIM DA CONTAGEM!')
