nome = str ( input ('Digite seu nome para análise : ')).strip().upper()
print ('Quantas vezes aparece a letra "A" na frase ? {}'.format (nome.count('A')))
print ('Em que posição ela aparece a primeira vez ? {}'.format (nome.find('A') +1))
print ('Em que posição ela aparece a ultima vez ? {}'.format(nome.rfind('A') +1))
