def leiaDinheiro(msg):
    reset = '\033[0;0m'
    vermelho = '\033[1;31m'
    while True:
        valor = str(input(msg))
        if valor.isnumeric():
            return float(valor)
            break
        else:
            print(f'{vermelho}{valor} não é válido!{reset}')
