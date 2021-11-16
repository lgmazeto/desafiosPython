import random

numero = int(input('Digite um número ente 0 e 5:'))
print('Você VENCEU!' if numero == random.randint(0,5) else 'Você PERDEU!')
