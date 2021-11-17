salario = float(str(input('Digite o salario:')).replace(',','.'))
if salario > 1250:
    print('Parabéns seu novo sálario é : R$ {:.2f}'.format(salario * 1.10))
else:
    print('Parabéns seu novo sálario é : R$ {:.2f}'.format(salario * 1.15))