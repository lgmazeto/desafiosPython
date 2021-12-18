from desafio_107 import moeda

valor = float(input('Digite o preço: R$ '))
print(f'Valor informado: {valor}')
print(f'Metade do valor {moeda.metade(valor)}')
print(f'Dobro do valor {moeda.dobro(valor)}')
print(f'Aumentar 10% > {moeda.aumentar(valor)}')
print(f'Diminuir 13% > {moeda.reduzir(valor)}')
