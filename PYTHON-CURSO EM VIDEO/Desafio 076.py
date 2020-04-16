
produtos = ('Monitor RazerX75', 1200,
           'Mouse RGB', 150,
           'Teclado Monster RGB', 320,
           'Caixa de Som', 50.99,
           'IphoneX', 2500,
           'Carregador', 20.90,
           'CPU-LAD', 450.99,
           'LAD-Xt80 1m', 15.50,
           'X-box360', 950.99,
           'Playstaion 4', 1550.90)
print ('_'*55)
print('{:^55}'.format('CHOICE WEB-DELIVRRE.COM'))
print ('°'*55)

c = 1
for x in range(len(produtos)):
    if x % 2 == 0:
        print(f'{c:^2} - {produtos[x]:.<39} R$',end='')
        c -= 1       # Pois o contador daria errado, pelo fato da razão dele ser 2
    if not x % 2 == 0:
        print(f'{produtos[x]:>8.2f}')
    c += 1
    
print('_'*55)
