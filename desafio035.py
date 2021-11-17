cores = {'limpa':'\033[m',
         'pretoebranco':'\033[40m'}

n1 = int(input('Digite o 1° número:'))
n2 = int(input('Digite o 2° número:'))
n3 = int(input('Digite o 3° número:'))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('{}Forma triangulo{}'.format(cores['pretoebranco'],cores['limpa']))
else:
    print('Não forma triangulo')