distancia = int(input('Digite a distancia em km'))
if distancia <= 200:
    print('Valor da passagem R$ {:.2f}'.format(distancia * 0.5))
else:
    print('Valor da passagem R$ {:.2f}'.format(distancia * 0.45))