def cadastrados():
    arquivo = open('desafio_115\cadastro.txt', 'rt')
    for cadastro in arquivo:
        ni = cadastro.split(',')
        for c in range(0, len(ni), 2):
            print(f'{ni[0].strip()}', end=' '*(35-len(ni[0].strip())-len(ni[1].strip())))
            print(f'{ni[1].strip()} anos')
    arquivo.close()
