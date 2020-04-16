cidade = str ( input ('Qual cidade você nasceu ? ')).strip().lower().split()
cidade = cidade[0]
print ('Sua cidade começa com a palavra Santo ? {}'.format('santo' in (cidade)))
