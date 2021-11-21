nota_50 = 0
nota_20 = 0
nota_10 = 0

valor_saque = int(input('Digite o valor para o saque:'))
while valor_saque >= 50:
    nota_50 += 1
    valor_saque = valor_saque - 50
while valor_saque >= 20:
    nota_20 += 1
    valor_saque = valor_saque - 20
while valor_saque >= 10:
    nota_10 += 1
    valor_saque = valor_saque - 10
if valor_saque == 0:
    print(f'Total de notas de 50: {nota_50}.\n'
          f'Total de notas de 20: {nota_20}.\n'
          f'Total de notas de 10: {nota_10}.\n')
else:
    print('O valor não pode ser sacado!')
