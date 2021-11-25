numeros = list()
valor = 0
while True:
    numero = int(input('Digite um valor:'))
    if numero in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(numero)
        print('Valor adicionado com sucesso...')
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')