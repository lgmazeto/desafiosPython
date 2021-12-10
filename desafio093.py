cadastro = dict()
gols = list()
soma = 0

cadastro['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
for p in range(0, partidas):
    gol = int(input(f'Número de gols na {p+1}° partida: '))
    soma += gol
    gols.append(gol)

cadastro['gols'] = gols.copy()
cadastro['total'] = soma

print('-'*80)
print(cadastro)
print('-'*80)

for k, v in cadastro.items():
    print(f'O campo {k} tem o valor: {v}')
print('-'*80)

print(f'O jogador {cadastro["nome"]} jogou {len(cadastro["gols"])} partidas.')
for p in range(0, partidas):
    print(f'    Na partida {p+1}, fez {cadastro["gols"][p]} gols.')
print(f'Foi um total de {soma}')
