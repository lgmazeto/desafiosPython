from time import sleep
from desafio_115 import opcao1, opcao2


def cabecalho(txt):
    print('-' * 40)
    print(txt.center(40))
    print('-' * 40)


def menu():
    green = '\033[1;32m'
    red = '\033[1;31m'
    blue = '\033[1;34m'
    yelow = '\033[1;33m'
    reset = '\033[0;0m'

    while True:
        cabecalho('MENU')
        print(f'{yelow}1 - {blue}Ver pessoas cadastradas')
        print(f'{yelow}2 - {blue}Cadastrar nova pessoa')
        print(f'{yelow}3 - {blue}Sair do sistema{reset}')
        print('-' * 40)

        try:
            opcao = int(input(f'{green}Sua opção: {reset}'))
        except ValueError:
            print(f'{red}Digite uma opção válida!{reset}')
            sleep(1)
            continue
        except KeyboardInterrupt:
            print(f'{red}Seleção interrompida, fechando o sistema.{reset}')
            break
        else:
            if opcao == 1:
                cabecalho('CADASTRADOS!')
                opcao1.cadastrados()
            elif opcao == 2:
                cabecalho('CADASTRAR!')
                opcao2.cadastrar()
            elif opcao == 3:
                cabecalho('Fechando o sistema!')
                break
            else:
                print(f'{red}Digite uma opção válida!{reset}')
                sleep(1)
                continue
