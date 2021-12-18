def leiaInt(msg='Leia um valor inteiro '):
    red = '\033[1;31m'
    reset = '\033[0;0m'
    while True:
        try:
            inteiro = int(input(msg))
        except KeyboardInterrupt:
            print(f'{red}O usuario não digitou o valor inteiro!{reset}')
            return 0
        except:
            print(f'{red}Erro, digite um valor inteiro válido!{reset}')
            continue
        else:
            return inteiro
            break


numero = leiaInt()
print(numero)
