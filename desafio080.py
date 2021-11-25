numeros = list()
for count in range(0, 5):
    numero = int(input('Digite um valor: '))
    if count == 0 or numero > numeros[-1]:
        numeros.append(numero)
    else:
        count = 0
        while count < len(numeros):
            if numero < numeros[count]:
                numeros.insert(count, numero)
                break
            count += 1

print(f'Lista ordenada sem sort() {numeros}')
