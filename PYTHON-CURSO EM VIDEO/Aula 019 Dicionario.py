# dicionario = {'nome':'Hero','idade': 19}
# dicionario['peso'] = 45.9  #Não precida do usar append()
# dicionario["genero"] = 'Masculino'
# del dicionario['peso']  
# print(f'O nome dele é: {dicionario["nome"]} e tem {dicionario["idade"]} anos')

# print (dicionario.keys()) # chaves 
# print (dicionario.values()) #valores
# print(dicionario.items())  #todos os itens 

# for keys, values in dicionario.items():
#     print (f'{keys} = {values}')

#----------------------------------------------------------------------

# dic = {'b': 4, 'a': 5, 'd': 1, 'c': 7}

# ordem = list(dic.keys())
# ordem.sort()

# for keys in ordem:
#     print (keys,dic[keys])    

# for k in sorted(dic):
#     print(f'{k} {dic[k]}')

from operator import itemgetter
# lista = [['emora',33],['aalnulsoo',32],['killer',12]]
# lista = {'bero':2,'canda':1,'aheu':3}

# lista.sort(key=itemgetter(1), reverse=True) #Não funciona para biblioteca 
# sorted(lista.items(),key=itemgetter(0))

