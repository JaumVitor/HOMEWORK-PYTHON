n= str(input('Data de nascimento: ')).split('/')
nasc = list()

for i in n:
	nasc.append(int(i))

idade = int (input ('Digite a idade para verificação : '))
new_year = nasc[2] + idade

new_date = list()
for idc, x in enumerate(nasc):
	if idc in (0,1):
		new_date.append(x)
	if idc == 2:
		new_date.append(new_year)
	
print (new_date)