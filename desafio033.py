n1 = int(input('Digite o 1° número:'))
n2 = int(input('Digite o 2° número:'))
n3 = int(input('Digite o 3° número:'))

#foi pasado o operador 'and', mas já tinha feito usando apenas ifs pra treinar.

if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print('Maior {}\n'
                  'Menor {}'
                  .format(n1, n3))
        else:
            print('Maior {}\n'
                  'Menor {}'
                  .format(n1, n2))
    else:
        if n2 > n3:
            print('Maior {}\n'
                  'Menor {}'
                  .format(n2, n3))
        else:
            print('Maior {}\n'
                  'Menor {}'
                  .format(n3, n2))
else:
    if n2 > n3:
        print('Maior {}\n'
              'Menor {}'
              .format(n2,n3))
    else:
        print('Maior {}\n'
              'Menor {}'
              .format(n1,n3))