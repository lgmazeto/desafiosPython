from math import fsum

gols = list()
players = list()
player = dict()
matchs = 0
totalGols = 0

while True:
    player['name'] = str(input('Player name: ')).strip().upper()
    matchs = int(input(f'How many matchs did {player["name"]} played? '))
    for m in range(0, matchs):
        gols.append(int(input(f'How many gols did {player["name"]} score in {m+1} match? ')))
    player['gols'] = gols.copy()
    player['total'] = int(fsum(gols))
    players.append(player.copy())
    gols.clear()
    player.clear()
    cont = str(input('Continue? [Y/N] ')).upper()[0]
    while True:
        if cont in 'YN':
            break
        else:
            cont = str(input('You must type YES [Y] or NO [N] ')).upper()[0]
    if cont in 'N':
        break

for n, p in enumerate(players):
    print(f'Player {n}:', end=' ')
    print(f'Data: {p}')

pl = 0
while pl != 999:
    while True:
        pl = int(input('More info about player number: (999 to OUT!)'))
        if pl <= len(players):
            print(f'Data about the player {players[pl]["name"]}')
            for m, g in enumerate(players[pl]['gols']):
                print(f'Match {m}, {g} scores.')
        elif pl == 999:
            break
        else:
            print('Valor invalido')
