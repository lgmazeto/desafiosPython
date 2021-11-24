produtos = 'Arroz', 29.90, 'Feijão', 10.58, 'Peixe', 40.85, 'Ovo', 8.50, 'Filé', 110.00

print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)

c = 0
for c in range(0,len(produtos),2):
    print(f'{produtos[c]:.<40}' + f'R$ {produtos[c+1]:>7.2f}')
