velocidade = int(input('Velocidade atual em km/h:'))
if velocidade > 80:
    print('Você foi MULTADO!\n'
          'Valor da multa R$ {},00'.format((velocidade - 80)*7))
else:
    print('Velocidade atual {} km/h'.format(velocidade))