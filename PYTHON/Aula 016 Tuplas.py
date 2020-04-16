fest = 'Hamburguer', 'Pizza', 'Refrigerante', 'Batata frita'

# for c in (fest):                    #Dessa maneira não é possivel fazer a contagem
#     print (f'Eu vou comer {c}')

for c in range (len(fest)):
    print(f'{c + 1}° = Eu vou comer {fest[c]}')

# for p, comida in enumerate (fest):
#     print(p + 1, comida)
