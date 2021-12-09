from random import randint
from time import sleep

dados = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}

for k, v in dados.items():
    sleep(1)
    print(f'O {k} tirou {v}')
print('-'*30)
for c in sorted(dados, key=dados.get, reverse=True):
    sleep(1)
    print(f'O {c}, tirou {dados[c]}')
