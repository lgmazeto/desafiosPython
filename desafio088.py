from random import randint
from time import sleep
jogos = list()
jogo = list()
numJogos = int(input('Quantos jogos deseja fazer? '))
while numJogos > 0:
    for c in range(0, 6):
        numero = randint(0, 60)
        if jogo.count(numero) > 0:
            numero = randint(0, 60)
        else:
            jogo.append(numero)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    numJogos -= 1
for pos, jg in enumerate(jogos):
    print(f'Jogo {pos+1}: {jg}')
    sleep(1)
