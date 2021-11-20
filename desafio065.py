n, soma, media, maior, menor = 0, 0, 0, 0, 9999
c = True
while c:
    valor = int(input('Digite um valor:'))
    soma += valor
    n += 1
    if maior < valor:
        maior = valor
    if menor > valor:
        menor = valor
    print('\nMédia {:.1f}\n'
          'Maior {}\n'
          'Menor {}\n'
          .format(soma/n, maior, menor))
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        c = False
