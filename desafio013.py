def aumento15pc(valor):
    return valor*1.15

valor = float(input('digite o salario para aumento de 15%'))
print('{} com 15% de aumento = {:.2f}'.format(valor, aumento15pc(valor)))