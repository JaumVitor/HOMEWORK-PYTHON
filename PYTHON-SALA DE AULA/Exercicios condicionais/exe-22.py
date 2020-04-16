data_nasc=input("nascimento:")
data_atual=input("data atual")
v_dtnasc=data_nasc.split("/")
v_dtatual=data_atual.split("/")

idade_ano = int(v_dtatual[2])- int(v_dtnasc[2])

idade_mes = ((idade_ano-1)*12)+int(v_dtatual[1]) 

idade_dia = ((idade_ano-1)*360)+((int(v_dtatual[1])-1)*30) +int(v_dtatual[0])

if int(v_dtatual[1])<int(v_dtnasc[1]):
    idade_ano-=1
elif int(v_dtatual[1])==int(v_dtnasc[1]):
    if int(v_dtatual[0])<int(v_dtnasc[0]):
        idade_ano-=1

print(str(idade_dia) +" dias" +str(idade_mes) +" meses" +str(idade_ano) +" anos" ) 
    
    

   
