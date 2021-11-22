classificacao = 'atletico mineiro', 'flamengo', 'palmeiras', 'corinthians',\
'fortaleza', 'bragantino', 'fluminense', 'internacional', 'ceara', 'america-mg',\
'cuiaba', 'santos', 'athetico-pr', 'sao paulo', 'atletico-go', 'juventude',\
'bahia', 'gremio', 'sport recife', 'chapecoense'
print(f'Primeiros 5 colocados da tabela {classificacao[:5]}')
print(f'Zona de reibaixamento {classificacao[-4:]}')
print(f'Times em ordem alfabetica {sorted(classificacao)}')
for time in classificacao:
    if time == 'chapecoense':
        print(f'Posicao da chape na tebela: {classificacao.index(time)+1}')
