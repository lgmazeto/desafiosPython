def fatorial(num, show=False):
    """
    -> Retorna o fatorial de um numero.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar conta.
    :return: O valor fatorial de numero.
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
        if show:
            if c == 1:
                print(f'{c} =', end=' ')
            else:
                print(f'{c} x', end=' ')
    return fat


numero = int(input('Digite um número: '))
print(fatorial(numero, show=True))
