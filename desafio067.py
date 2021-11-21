valor, count = 0, 0
while valor >= 0:
    valor = int(input('Digite um valor para calcular a tabuada:'))
    if valor < 0:
        break
    while count <= 10:
        print(f'{valor} * {count} = {valor * count}')
        count += 1
        if count > 10:
            count = 0
            break
print('Programa encerrado')