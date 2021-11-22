from random import randint

valoresAleatorios = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(valoresAleatorios)
print(f'Menor valor na tupla {min(valoresAleatorios)}')
print(f'Maior valor na tupla {max(valoresAleatorios)}')