palavras = 'arroz', 'batata', 'ovo', 'carne', 'arvore', 'estrela', 'azul', 'navio'

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos as vogais: ', end='')
    for vogais in palavra:
        if vogais.upper() in 'AEIOU':
            print(vogais, end=' ')
    print('')
