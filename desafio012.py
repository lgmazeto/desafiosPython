def desconto5pc(valor):
    return valor*0.95

valor = float(input('digite o valor para desconto 5%'))
print('{} com 5% de desconto = {:.2f}'.format(valor,desconto5pc(valor)))