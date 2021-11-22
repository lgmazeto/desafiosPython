valor1 = int(input("digite o valor:"))
valor2 = int(input("digite o valor:"))
valor3 = int(input("digite o valor:"))
valor4 = int(input("digite o valor:"))

valores = valor1, valor2, valor3, valor4

print(f'valor 9 apareceu {valores.count(9)} vezes.')

if 3 in valores:
    print(f'o valor 3 aparece primeiro na posicao {valores.index(3)}')

for valor in valores:
    if valor % 2 == 0:
        print(f'valor par {valor}')
