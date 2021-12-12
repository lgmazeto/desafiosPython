cadastro = dict()
cadastros = list()
sexoF = list()
idadeAcimaDaMedia = list()
idadeMedia = 0

while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo: [M/F] '))
    cadastro['idade'] = int(input('Idade: '))
    cadastros.append(cadastro.copy())
    continuar = str(input('Novo cadastro: [S/N] '))
    if continuar in 'Nn':
        break

for d in cadastros:
    idadeMedia += d['idade']
    if d['sexo'] in 'Ff':
        sexoF.append(d['nome'])
idadeMedia /= len(cadastros)

for d in cadastros:
    if d['idade'] > idadeMedia:
        idadeAcimaDaMedia.append(d['nome'])

print(f'Numero de pessoas cadastradas: {len(cadastros)}')
print(f'A media de idade do grupo: {int(idadeMedia)}')
print(f'Mulheres cadastradas: {sexoF}')
print(f'Pessoas com idade acima da media: {idadeAcimaDaMedia}')
