def metade(valor, formatar=False):
    resultado = valor * 0.5
    return moeda(resultado) if formatar else resultado


def dobro(valor, formatar=False):
    resultado = valor * 2
    return moeda(resultado) if formatar else resultado


def aumentar(valor, percentual, formatar=False):
    resultado = valor * (1 + (percentual / 100))
    return moeda(resultado) if formatar else resultado


def reduzir(valor, percentual, formatar=False):
    resultado = valor * (1 - (percentual / 100))
    return moeda(resultado) if formatar else resultado


def moeda(valor):
    return f'R$ {valor:.2f}'


def resumo(valor, aumento, reducao):
    print(f'Valor informado: {moeda(valor)}')
    print(f'Metade do valor {metade(valor)}')
    print(f'Dobro do valor {dobro(valor)}')
    print(f'Aumentar {aumento}% > {aumentar(valor, aumento, True)}')
    print(f'Diminuir {reducao}% > {reduzir(valor, reducao, True)}')
