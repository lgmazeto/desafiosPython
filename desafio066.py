valor, soma, n = 0, 0, 0
while valor != 999:
    valor = int(input('Digite um valor:'))
    if valor == 999:
        break
    soma += valor
    n += 1

print(f'A soma dos {n} valores é {soma}')
