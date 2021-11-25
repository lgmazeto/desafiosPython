numeros = list()
posMaior = list()
posMenor = list()

for count in range(0, 5):
    numeros.append(int(input('Digite um valor:')))

maior = max(numeros)
menor = min(numeros)

for pos, numero in enumerate(numeros):
    if numero == maior:
        posMaior.append(str(pos) + '... ')
    if numero == menor:
        posMenor.append(str(pos) + '... ')

print(f'O maior numero é o {maior} e sua posição é {posMaior}')
print(f'O maior numero é o {menor} e sua posição é {posMenor}')
