from time import sleep
km = str ( input ('Digite quantos quilometros equivalem  a viagem : ')).upper().strip()

sleep(2)
print('vc está prestes a iniciar uma viagem de {}km'.format(km))
sleep(2)
print ('Aguarde um instante....')
sleep(3)

# if  float( km ) <= 200 :
#     custo = float( km )  * 0.50
# else:
#     custo = float( km ) * 0.45
# print ('Custo da viagem será de R${:.2f}'.format(custo))

custo = 0.50 * float( km )  if ( float( km )<= 200) else 0.45 *float( km )
print ( 'Custo da vigem será de R${:.2f}'.format(custo))
