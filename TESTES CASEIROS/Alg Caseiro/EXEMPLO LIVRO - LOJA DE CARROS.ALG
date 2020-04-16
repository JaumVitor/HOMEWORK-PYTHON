Algoritmo "EXEMPLO LIVRO"

Var
    p_fab , pc_lucroDT , pc_imposto : REAL
    LUCRO_DT , VALOR_IMPOSTO , P_FINAL : REAL
Inicio
      ESCREVAL (":::::::::::::::::::::::::::::::::::::::::")
      ESCREVAL ("LOJA DE CARROS IRADOS, COMPRE JÁ O SEU !!")
      ESCREVAL (":::::::::::::::::::::::::::::::::::::::::")
      ESCREVAL("")

       ESCREVA ("DIGITE O PREÇO DE FABRICA: ")
      LEIA (p_fab)
      ESCREVA ("ESCREVA O PERCENTUAL DO LUCRO DO DISTRIBUIDOR: ")
      LEIA (pc_lucroDT)
      ESCREVA ("ESCREVA PERCENTUAL DE IMPOSTO: ")
      LEIA (pc_imposto)
      
      LUCRO_DT  <- ( p_fab * pc_lucroDT / 100 )
      VALOR_IMPOSTO  <- ( p_fab * pc_imposto / 100 )
      P_FINAL  <- ( p_fab + LUCRO_DT + VALOR_IMPOSTO )
      ESCREVAL ("")
      
      ESCREVAL ("LUCRO OBTIDO PELO DISTRIBUIDOR:", LUCRO_DT)
      ESCREVAL ("VALOR DOS IMPOSTOS:", VALOR_IMPOSTO)
      ESCREVAL ("PREÇO TOTAL DO CARRO:", P_FINAL)


Fimalgoritmo