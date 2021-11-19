numero = int(input('Digite um valor para ser convertido:\n'))
opcao = int(input('Converter:\n'
                  '1 - Decimal\n'
                  '2 - Octal\n'
                  '3 - Hexadecimal\n'))
if opcao == 1:
    print('Valor do numero em binario: {}'.format(bin(numero)[2:]))
elif opcao == 2:
    print('Valor do numero em octal: {}'.format(oct(numero)[2:]))
elif opcao == 3:
    print('Valor do numero em hexadecimal: {}'.format(hex(numero)))
else:
    print('Coversao invalida!')