largura = float(input('digite o valor da largura'))
altura = float(input('digite o valor da altura'))
area = largura * altura
print('area da parede = {:.2f}\n'
      'será necessario {:.1f} litros para pintar a parede'.format(
    area, area/2))
