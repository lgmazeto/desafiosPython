def total(distacia, dias):
    return (distacia*0.15 + dias*60)

distacia = float(input('quilometros rodados'))
dias = int(input('dias alugados'))
print('o carro rodou {} km durante {} dias\n'
      'total a pagar R$ {:.2f}'.format(distacia, dias, total(distacia,dias)))
