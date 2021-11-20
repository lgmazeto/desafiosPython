num = int(input('Elementos da sequencia:'))
fibonacci = 0
c = 0
anterior1 = 1
anterior2 = 0
while c <= num:
    print('{} elemento, fibonacci {}'.format(c, fibonacci))
    anterior2 = anterior1
    anterior1 = fibonacci
    fibonacci = anterior2 + anterior1
    c += 1

