from datetime import datetime

ano_nascimento = int(input('Ano de nascimento: '))

def voto():
	idade = datetime.now().year - ano_nascimento
	if 15 < idade < 18 or idade > 65:
		return (f'Com {idade} anos de idade: VOTO opicional!')
	elif idade >= 18:
		return (f'Com {idade} anos de idade: VOTO obrigatório!')
	else:
		return (f'Com {idade} anos de idade: NÃO VOTA! ')

print (voto())
	


