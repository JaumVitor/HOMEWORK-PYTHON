print('-=' * 20)
casa = float ( input ('Qual o valor da casa ? '))
salario = float ( input ('Quanto vc recebe de salário ? '))
anos = int ( input ('Por quantos anos pretende pagar a casa ? '))
print ('-=' * 20)
mensalidade = casa / (anos * 12)

if mensalidade > salario * 0.30:
    print('''A casa tem um custo de R${:.2f}, em {} anos você terá uma mensalidade de R${:.2f},
infelizmente seu financiamento foi negado, por seu salário não ser adequado para quitar sua divida :('''.format(casa , anos , mensalidade))
elif mensalidade <= salario * 0.30:
    print('''A casa tem um custo de R${:.2f}, em {} anos você terá uma mensalidade de R${:.2f}, então PARABÉNS
agora pode agendar seu financiamento'''.format(casa , anos , mensalidade))
print('-=' * 20)
