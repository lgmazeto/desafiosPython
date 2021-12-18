from desafio_107 import moeda

valor = float(input('Digite o preço: R$ '))
print(f'Valor informado: {moeda.moeda(valor)}')
print(f'Metade do valor {moeda.moeda(moeda.metade(valor))}')
print(f'Dobro do valor {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentar 10% > {moeda.moeda(moeda.aumentar(valor))}')
print(f'Diminuir 13% > {moeda.moeda(moeda.reduzir(valor))}')
