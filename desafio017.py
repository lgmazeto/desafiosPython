import math
coposto = float(input('Cateto oposto: '))
cadjacente = float(input('Cateto adjacente: '))
hipotenusa = math.hypot(coposto,cadjacente)
print('hipotenusa = {:.2f}'.format(hipotenusa))
