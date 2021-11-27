pessoas = list()
pesoMaior = list()
pesoMenor = list()
maior, menor = 0, 9999
while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    pessoas.append([nome, peso])
    continuar = str(input('Desaja continuar? [S/N]')).strip()
    if continuar in 'Nn':
        break
for pessoa in pessoas:
    if pessoa[1] > maior:
        maior = pessoa[1]
    if pessoa[1] < menor:
        menor = pessoa[1]
for pessoa in pessoas:
    if pessoa[1] == maior:
        pesoMaior.append(pessoa[0])
    if pessoa[1] == menor:
        pesoMenor.append(pessoa[0])

print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso foi {maior}, pessoas mais pesadas: {pesoMaior}')
print(f'O menor peso foi {menor}, pessoas mais leves: {pesoMenor}')