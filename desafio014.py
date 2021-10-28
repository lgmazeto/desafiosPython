def converter(valor):
    return (valor*(9/5))+32

valor = float(input('digite a temperatura em graus'))
print('temperatura em fahrenheit = {:.0f}'.format(converter(valor)))
