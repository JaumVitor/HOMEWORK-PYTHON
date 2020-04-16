pro1 = float ( input ( 'Preço do Prmeiro produto ? '))
pro2 = float ( input ( 'Preço do Segundo produto ? '))
pro3 = float ( input ( 'Preço do Terceiro produto ? '))

if (  pro2 > pro1 < pro3 ) :
   print ('Produto 1 é mais barato...Esse deve ser comprado ')
elif(  pro1 > pro2 < pro3 ):
   print ('Segundo produto é mais barato....Esse deve ser comprado ')
elif(  pro1 > pro3 < pro2 ):
   print ('Terceiro produto é mais barato....Esse deve ser comprado ')
