import random

jogador = str(input('Pedra, papel ou tesoura?')).upper().strip()
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
ai = random.choice(opcoes)

if jogador == ai:
    print('Empate')
elif jogador == 'PEDRA' and ai == 'TESOURA':
    print('Vitoria jogador')
elif jogador == 'PAPEL'and ai == 'PEDRA':
    print('Vitoria jogador')
elif jogador == 'TESOURA' and ai == 'PAPEL':
    print('Vitoria jogador')
else:
    print('Vitoria do computador')

