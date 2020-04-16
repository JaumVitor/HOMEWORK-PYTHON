#Jogadores de futebol exercicio 093/1 - Guanabara

inf = dict()
gols = list()
lista = list()  #Todos os jogadores 

while True:
    inf['nome'] = str(input('Nome: '))
    n = int(input(f'*> Quantas partidas {inf["nome"].upper()} jogou ? '))
    print('-')

    for c in range(1, n + 1):
        gols.append(int(input(f'*> Quantos gols na {c}º partida ? ')))
        inf['marcou'] = gols[:]

    inf['total'] = sum(inf['marcou'])

    print ()

    lista.append(inf.copy())
    gols.clear()

# PARTE DA FINALIZAÇÃO ?...PERGUNTA SE O USUÁRIO QUER OU NÃO CONTINUAR 

    while True:
        next = str(input('   *> Quer prosseguir |Sim/Não| ? ')).upper()[0]

        if next in 'NS':
            if next in 'S':
                print('=' * 52)
            if next in 'N':
                print ()
            break
        else:
            print('       // Digite uma opção válida! "Sim ou Não"\n')
            
    if next in 'N':     #Apos a saida do looping 
        break

#Parte da tabela dos jogadores 
print('_'*68)
print('|{:^3}|{:^20}|{:^20}|{:^20}|'.format('Nº', 'JOGADORES', 'GOLS', 'TOTAL'))
print ('-'*68)
for n,x in enumerate(lista):
    print(f'|{n + 1}º |', end='')
    for v in x.values():
        print (f'{str(v):^20}|',end='')
    print ()    
    
print ('='*68)

while True:
    jogador = int (input ('*> Quer ver os dados de qual jogador ? '))
    if jogador == 999: 
        break

    if jogador == 0:        #Caso o valor zero seja digitado! 
        while True:
            if jogador == 0:
                print(
                    '    // Jogador ZERO não existe...digite um valor válido! \n')
            else:
                print(
                    '    // JOGADOR INESISTENTE, TENTE NOVAMENTE \n')

            jogador = int(input('*> Quer ver os dados de qual jogador ? (Encerramento = 999) '))
            if jogador == 999:
                break
            if (jogador <= len(lista)) and jogador != 0:
                break

    if jogador == 999:
        break
            
    if jogador <= len(lista):
        print ()
        print ('-='*26)
        print(
            f'    <****( DESENPENHO DO JOGADOR {lista[jogador - 1]["nome"].upper()} )****>')
       
        for c,v in enumerate (lista[jogador - 1]["marcou"]):
            print(f'- {c:>10}º JOGO: {lista[jogador - 1 ]["nome"]} marcou {v}')
        print ('-+'* 26,'\n')
    else:
        print(
            '    // JOGADOR INESISTENTE, TENTE NOVAMENTE...(Encerramento = 999)! \n')
    
