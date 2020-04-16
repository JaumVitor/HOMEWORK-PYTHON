print('{:-^40}\nPrograma para dizer:\n'.format(str('Desafio 22')))
nome = input('Digite seu nome completo: ')
dividido = nome.split()
nospace = ''.join(dividido)
print(f"""\nMaiusculo: {nome.upper()}
Minusculo: {nome.lower()}
Seu nome tem {len(nospace)} letras ao todo (desconsiderando espaço)
Primeiro nome tem {len(dividido[0])} letras""")
