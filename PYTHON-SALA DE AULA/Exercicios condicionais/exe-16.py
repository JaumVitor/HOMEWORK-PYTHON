alt = float ( input ('Qual sua altura ? '))
massa = float ( input ('Qual sua massa corporal ? '))
imc = (massa / (alt ** 2))
if (imc <= 25):
    print ('IMC >>> NORMAL')
elif (30 > imc > 25):
    print ('IMC >>> OBESO')
elif (imc > 30):
    print ('IMC >>> OBESIDSDE MORBIDA') 