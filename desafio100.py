from random import randint

def sorteia():
    sorteados = list()
    for c in range(0, 5):
        sorteados.append(randint(0, 10))
    return sorteados

def somaPar(sorteados):
    soma = 0
    for num in sorteados:
        print(num, end=' ')
        if num % 2 == 0:
            soma += num
    print()
    print(f'Soma dos valores pares: {soma}')


somaPar(sorteia())
