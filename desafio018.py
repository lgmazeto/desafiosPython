import math
angulo = float(input('Digite o angulo em graus: '))
angulo = math.radians(angulo)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('seno = {:.2f}\ncosseno = {:.2f}\ntangente ={:.2f}'
      .format(seno, cosseno, tangente))