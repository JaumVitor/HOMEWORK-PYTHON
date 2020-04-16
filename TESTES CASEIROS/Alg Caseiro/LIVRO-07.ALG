algoritmo "LIVRO-07"
var
   PESO1,PESO2,R1,R2,PESO: real
   
inicio
      ESCREVA ("DIGITE O PESO em Kg: ")
      LEIA (PESO)
      PESO1 <- (PESO * 0.15)
      PESO2 <- (PESO * 0.20)
      R1 <- (PESO + PESO1)
      R2 <- (PESO - PESO2)
      
      ESCREVAL ("PESO COM AUMENTO DE 15%: ",R1," Kg")
      ESCREVAL ("PESO COM REDUÇÃO DE 20%: ",R2," Kg")
fimalgoritmo