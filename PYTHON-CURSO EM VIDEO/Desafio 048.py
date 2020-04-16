soma = 0 
cont = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        soma += impar  # poderia ter escrito de outra forma [soma = soma + impar] 
        cont += 1      # poderia ter escrito de outra forma [cont = cont + 1 ]
print ('A soma dos números analisados é {}, e foram usados {} números para a contagem '.format( soma, cont  ) )
