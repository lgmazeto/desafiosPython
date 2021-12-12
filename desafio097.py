def escreva(msg):
    tamanho = len(msg)
    print('~'*tamanho*2)
    print(' ' * int(tamanho*0.5) + msg)
    print('~'*tamanho*2)


escreva('Posso escrever qualquer coisa!')