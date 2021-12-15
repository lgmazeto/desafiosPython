def leiaInt(msg='Leia um valor inteiro '):
    inteiro = str(input(msg))[0]
    while not inteiro.isnumeric():
        if inteiro.isnumeric():
            return int(inteiro)
        else:
            print(f'\33[0:31m ->Erro! valor inválido! \033[0;0m')
        inteiro = str(input(msg))[0]
    return inteiro


numero = leiaInt()
print(numero)
