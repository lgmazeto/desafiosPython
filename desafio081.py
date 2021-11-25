numeros = list()
while True:
    numeros.append(int(input('Digite um numero: ')))
    cont = str(input('Deseja continuar? [S/N]')).strip()
    if cont in 'Nn':
        break
print(f'Os numeros digitados foram: {numeros}')
print(f'Total de numeros digitados: {len(numeros)}')
numeros.sort(reverse=True)
print(f'A lista em onder decrescente: {numeros}')
print('Na lista contem o valor 5' if numeros.index(5) > 0 else 'Não ha valor 5 na lista')
