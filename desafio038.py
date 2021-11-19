def maior(a, b):
    if a > b:
        return print('1° maior = {}\n'
                     '2° maior = {}'
                     .format(a, b))
    elif a == b:
        return print('Os valores são iguais {} = {}'
                     .format(a, b))
    else:
        return print('1° maior = {}\n'
                     '2° maior = {}'
                     .format(b, a))


n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
maior(n1,n2)