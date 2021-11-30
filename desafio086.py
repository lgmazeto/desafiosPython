matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for m in range(0, 3):
    for n in range(0, 3):
        matriz[m][n] = int(input(f'Digite o valor para [{m}, {n}]: '))
for m in range(0, 3):
    for n in range(0, 3):
        print(f'[{matriz[m][n]:^5}]', end='')
    print()
print('-'*50)

par = soma = 0
for c in range(0, 3):
    for numero in matriz[c]:
        if numero % 2 == 0:
            par += numero
    soma += matriz[c][2]
maior = max(matriz[1])
print(f'A soma dos valores pares é: {par}')
print(f'A soma dos valores da terceira coluna é: {soma}')
print(f'O maior valor da segunda linha é: {maior}')
