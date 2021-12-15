def ajuda(item):
    while item != 'FIM':
        help(item)
        item = str(input('Deseja mais alguma informação?')).lower().strip()
        if item == 'fim':
            print('Volte sempre!')
            break


item = str(input('Pergunte sobre uma função...')).lower().strip()
ajuda(item)
