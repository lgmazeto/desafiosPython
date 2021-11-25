numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um numero: ')))
    cont = str(input('Deseja continuar? [S/N]')).strip()
    if cont in 'Nn':
        break
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'Lista dos numeros digitados: {numeros}')
print(f'Lista dos numeros pares: {pares}')
print(f'Lista dos numeros impares: {impares}')
